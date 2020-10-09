import json
import png
import sys
import math

from shapes import Material, Sphere, Plane, PointLight
from vector import Vector, Ray

EPSILON = 1e-6

def parse_color(json):
    return Vector(json['red'], json['green'], json['blue'])

def parse_vector(json):
    return Vector(json['x'], json['y'], json['z'])

def parse_material(json):
    return Material(parse_color(json['color']), json['ambient'], json['diffuse'])

def closest_intersection(shapes, ray):
    closest_shape = None
    intersection = None
    for shape in shapes:
        t = shape.intersect(ray)
        if t is None or t < EPSILON:
            continue
        if intersection is None or t < intersection:
            closest_shape = shape
            intersection = t
    return closest_shape, ray.at(intersection) if intersection else None

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

    shapes = []
    for shape_data in scene_data['shapes']:
        shape_type = shape_data['type']
        if shape_type == 'sphere':
            shapes.append(Sphere(
                parse_vector(shape_data['transform']['translate']),
                shape_data['radius'],
                parse_material(shape_data['material'])
            ))
        elif shape_type == 'plane':
            shapes.append(Plane(
                parse_vector(shape_data['transform']['translate']),
                Vector(0.0, 1.0, 0.0),
                parse_material(shape_data['material'])
            ))

    lights = [
        PointLight(
            parse_vector(light_data['transform']['translate']),
            parse_color(light_data['color']),
            light_data['intensity']
        )
        for light_data in scene_data['lights']
        if light_data['type'] == 'point'
    ]

    image_data = []
    for y in range(height):
        row_data = []
        for x in range(width):
            camera_ray = Ray(
                Vector(0, 0, 0),
                Vector(x - (width / 2), (width / 2) - y, depth).normalize()
            )

            closest_shape, intersection = closest_intersection(shapes, camera_ray)

            if closest_shape != None:
                final_color = closest_shape.material.color.scale(closest_shape.material.ambient)
                for light in lights:
                    light_vector = light.position.subtract(intersection)
                    light_ray = Ray(intersection, light_vector.normalize())
                    if closest_intersection(shapes, light_ray)[0] is not None:
                        continue
                    normal_factor = max(0, closest_shape.normal_at(intersection).dot(
                        light_vector.normalize()
                    ))
                    final_color = final_color.add(
                        closest_shape.material.color.multiply(light.color)
                        .scale(closest_shape.material.diffuse * normal_factor * light.intensity / light_vector.length())
                    )
                row_data += final_color.to_bytes()
            else:
                row_data += background_color.to_bytes()
        image_data.append(row_data)

    writer = png.Writer(width, height, greyscale=False)
    with open(argv[2], 'wb') as output_file:
        writer.write(output_file, image_data)

if __name__ == '__main__':
    main(sys.argv)