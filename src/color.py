def to_byte(value):
    return max(0, min(255, int(255 * value)))

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def to_bytes(self):
        return [to_byte(self.red), to_byte(self.green), to_byte(self.blue)]