# python-raytracer

This is an example raytracer used for teaching.

## Checkpoints

The implementation is split into checkpoints. Students should reach each checkpoint and verify that their program produces the same output as the sample image before moving on to the next checkpoint. The sample scene is at `scenes/test.json`.

### 1: Write an image

Read a scene description file and output file name from a command line arguments. Parse the scene description file. Write a PNG file to the specified file name that has the width, height, and world background color specified in the scene description. Colors in the description file are specified on a zero to one scale for each primary component (red, green, and blue).

    python src/raytracer.py scenes/test.json render.png

![Checkpoint 1 render](renders/checkpoint_1.png?raw=true)

### 2: Draw sphere silhouettes

Read `camera` and `shapes` from the scene description, but only the shapes where `type` is `sphere`. The coordinate system is assumed to have positive x going to the right, positive y going up, and positive z going into the screen. The camera is assumed to be at (0, 0, 0) and `field_of_view` specifies the horizontal field of view of the camera in degrees. Each sphere has a radius specified by `radius` and is centered at the position specfied by the x, y, and z values in `translate`.

Generate a camera ray for each pixel in the image and find the first shape, if any, that the ray intersects. Color the pixel the color of that shape (from the `material`), or the background color if the ray doesn't hit anything.

![Checkpoint 2 render](renders/checkpoint_2.png?raw=true)

### 3: Add diffuse and ambient shading

Read `lights` from the scene description. Each point light source is centered at the position specified by the x, y, and z values in `translate` and has an intensity specified by `intensity` 1 unit away from the center. Intensity falls off with distance according to the [inverse square law](https://en.wikipedia.org/wiki/Inverse-square_law). The color of each light source is specified by `color`.

Each point on a shape should be shaded according to this formula, where `normal_factor` is the dot product of a unit vector pointing from the point to the light source with a unit vector pointing away from the center of the sphere (a [normal vector](https://en.wikipedia.org/wiki/Normal_(geometry))). This is known as [Lambertian reflectance](https://en.wikipedia.org/wiki/Lambertian_reflectance). `light_color` and `shape_color` should be piecewise multiplied. For example, a red shape in a green light should appear black.

    final_color = ambient * shape_color + diffuse * normal_factor * light_color * intensity * shape_color * (1 / distance^2)

![Checkpoint 3 render](renders/checkpoint_3.png?raw=true)