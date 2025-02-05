class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be of same length")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be of same length")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def __str__(self):
        return f'Vector({', '.join(map(str, self.coordinates))})'
    
    def __len__(self):
        return len(self.coordinates)

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])
c = a + b
print(c)  # Output: Vector(5, 7, 9)
d = a * b
print(d)  # Output: 32
print(len(a))  # Output: 3