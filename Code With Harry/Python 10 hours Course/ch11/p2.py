class Pets:
    a = 'It is a pet.'
    # a = 'It is a pet.'

class Animals(Pets):
    a = 'It is an animal.'
    # b = 'It is an animal.'

class Dog(Animals):
    a = 'It is a dog.'
    # c = 'It is a dog.'
    def bark(self):
        print('The dog is barking.')

x = Dog()
print(x.a)
# print(x.b)
# print(x.c)
x.bark()

y = Pets()
print(y.a)

z = Animals()
print(z.a)