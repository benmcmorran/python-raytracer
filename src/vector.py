import math

def to_byte(value):
    return max(0, min(255, int(255 * value)))

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
    
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def multiply(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def to_bytes(self):
        return [to_byte(self.x), to_byte(self.y), to_byte(self.z)]

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
    def at(self, t):
        return self.origin.add(self.direction.scale(t))