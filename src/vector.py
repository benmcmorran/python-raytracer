import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.dot(self))

    def scale(self, factor):
        return Vector(factor * self.x, factor * self.y, factor * self.z)

    def normalize(self):
        return self.scale(1 / self.length())

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction