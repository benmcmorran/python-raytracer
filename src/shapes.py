import math

class Material:
    def __init__(self, color, ambient, diffuse):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

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

class Plane:
    def __init__(self, origin, normal, material):
        self.origin = origin
        self.normal = normal
        self.material = material
    
    def intersect(self, ray):
        alignment = ray.direction.dot(self.normal)
        if alignment == 0:
            return None

        t = self.origin.subtract(ray.origin).dot(self.normal) / alignment
        if t >= 0:
            return t
        return None
    
    def normal_at(self, point):
        return self.normal

class PointLight:
    def __init__(self, position, color, intensity):
        self.position = position
        self.color = color
        self.intensity = intensity