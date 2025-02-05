class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, other):
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
    def __str__(self):
        return f'{self.x}i + {self.y}j + {self.z}k'

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
c = a + b
print(c)
d = a * b
print(d)
