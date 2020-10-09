import math

class Sphere:
    def __init__(self, center, radius, color, ambient, diffuse):
        self.center = center
        self.radius = radius
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse

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
    
    def normal_at(self, point):
        return point.subtract(self.center).normalize()

class PointLight:
    def __init__(self, position, color, intensity):
        self.position = position
        self.color = color
        self.intensity = intensity