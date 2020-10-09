import math

class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersect(self, ray):
        offset = ray.origin.subtract(self.center)
        b = ray.direction.dot(offset)
        discriminant = b ** 2 - offset.dot(offset) + self.radius ** 2

        if discriminant < 0:
            return None

        t = -b - math.sqrt(discriminant)
        if t >= 0:
            return t
        return -b + math.sqrt(discriminant)
