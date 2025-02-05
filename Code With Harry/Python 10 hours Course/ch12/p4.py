try:
    a: int = int(input("Enter a number: "))
    b: int = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed.")