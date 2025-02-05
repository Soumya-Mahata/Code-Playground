marks1 = int(input('Enter the marks of Physics (Out of 100): '))
marks2 = int(input('Enter the marks of Chemistry (Out of 100): '))
marks3 = int(input('Enter the marks of Mathematics (Out of 100): '))
total_percentage = (marks1 + marks2 + marks3) / 3

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print(f'You passed: Your percentage = {total_percentage}')
else:
    print(f'You failed: Your percentage = {total_percentage}')