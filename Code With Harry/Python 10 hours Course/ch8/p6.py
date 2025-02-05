def inches_to_cms(n):
    return 2.54 * n

i = int(input('Enter the amount in inches: '))
c = inches_to_cms(i)
print(f'{i}inches = {round(c, 2)}centimeters')