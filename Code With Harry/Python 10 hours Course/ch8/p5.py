def star(n):
    for i in range(n):
        print('*' * (n - i))

n = int(input('Enter the number: '))
star(n)