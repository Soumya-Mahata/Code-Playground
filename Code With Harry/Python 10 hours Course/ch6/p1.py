num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))
num4 = int(input('Enter 4th number: '))

if num1 >= num2:
    greater_num = num1
else:
    greater_num = num2

if num3 >= greater_num:
    greater_num = num3

if num4 >= greater_num:
    greater_num = num4

print(f'Greatest number is {greater_num}')

