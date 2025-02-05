class Calculator:

    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f'{self.num} ^ 2 = {self.num ** 2}')

    def cube(self):
        print(f'{self.num} ^ 3 = {self.num ** 3}')

    def square_root(self):
        print(f'{self.num} ^ (1/2) = {self.num ** (1/2)}')

    @staticmethod
    def greet():
        print('Hello! Thank You for using the Calculator.\n')

    
calculate = Calculator(int(input('Enter the number: ')))
calculate.square()
calculate.cube()
calculate.square_root()
calculate.greet()