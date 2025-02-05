obtained_marks = int(input("Enter your marks here: "))

if (100 > obtained_marks >= 90):
    grade = 'Ex'
elif (90 > obtained_marks >= 80):
    grade = 'A'
elif (80 > obtained_marks >= 70):
    grade = 'B'
elif (70 > obtained_marks >= 60):
    grade = 'C'
elif (60 > obtained_marks >= 50):
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}")