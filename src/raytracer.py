import json
import png
import sys

from color import Color

def parse_color(json):
    return Color(json['red'], json['green'], json['blue'])

def main(argv):
    if len(argv) != 3:
        print('Usage: python raytracer.py <scene file> <output file>')
        sys.exit(1)

    with open(argv[1], 'r') as scene_file:
        scene_data = json.load(scene_file)
    
    width = scene_data['output']['width']
    height = scene_data['output']['height']
    background_color = parse_color(scene_data['world']['color'])

    image_data = []
    for y in range(height):
        row_data = []
        for x in range(width):
            row_data += background_color.to_bytes()
        image_data.append(row_data)

    writer = png.Writer(width, height, greyscale=False)
    with open(argv[2], 'wb') as output_file:
        writer.write(output_file, image_data)

if __name__ == '__main__':
    main(sys.argv)