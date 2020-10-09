# python-raytracer

This is an example raytracer used for teaching.

## Checkpoints

The implementation is split into checkpoints. Students should reach each checkpoint and verify that their program produces the same output as the sample image before moving on to the next checkpoint. The sample scene is at `scenes/test.json`.

### 1: Write an image

Read a scene description file and output file name from a command line arguments. Parse the scene description file. Write a PNG file to the specified file name that has the width, height, and world background color specified in the scene description. Colors in the description file are specified on a zero to one scale for each primary component (red, green, and blue).

    python src/raytracer.py scenes/test.json render.png

![Checkpoint 1 render](renders/checkpoint_1.png?raw=true)