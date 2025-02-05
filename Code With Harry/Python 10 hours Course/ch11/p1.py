class two_D_vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'The 2d vector is {self.x}i + {self.y}j')

class three_D_vec(two_D_vec):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(f'The 3d vector is {self.x}i + {self.y}j + {self.z}k')

a = two_D_vec(2, 3)
b = three_D_vec(5, 1, 6)
a.show()
b.show()
