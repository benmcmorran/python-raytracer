import json
import png
import sys
import math

from shapes import Sphere
from color import Color
from vector import Vector, Ray

def parse_color(json):
    return Color(json['red'], json['green'], json['blue'])

def parse_vector(json):
    return Vector(json['x'], json['y'], json['z'])

def main(argv):
    if len(argv) != 3:
        print('Usage: python raytracer.py <scene file> <output file>')
        sys.exit(1)

    with open(argv[1], 'r') as scene_file:
        scene_data = json.load(scene_file)
    
    width = scene_data['output']['width']
    height = scene_data['output']['height']
    fov = scene_data['camera']['field_of_view']
    depth = (width / 2) / math.tan((fov / 2) * (math.pi / 180))

    background_color = parse_color(scene_data['world']['color'])

    shapes = [
        Sphere(
            parse_vector(shape_data['transform']['translate']),
            shape_data['radius'],
            parse_color(shape_data['material']['color'])
        )
        for shape_data in scene_data['shapes']
        if shape_data['type'] == 'sphere'
    ]

    image_data = []
    for y in range(height):
        row_data = []
        for x in range(width):
            camera_ray = Ray(
                Vector(0, 0, 0),
                Vector(x - (width / 2), (width / 2) - y, depth).normalize()
            )
            closest_shape = None
            closest_intersection = None
            for shape in shapes:
                t = shape.intersect(camera_ray)
                if t is None:
                    continue
                if closest_intersection is None or t < closest_intersection:
                    closest_shape = shape
                    closest_intersection = t
            if closest_shape != None:
                row_data += closest_shape.color.to_bytes()
            else:
                row_data += background_color.to_bytes()
        image_data.append(row_data)

    writer = png.Writer(width, height, greyscale=False)
    with open(argv[2], 'wb') as output_file:
        writer.write(output_file, image_data)

if __name__ == '__main__':
    main(sys.argv)