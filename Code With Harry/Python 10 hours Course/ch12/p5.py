n = int(input("Enter a number: "))
table = [(i * n) for i in range(1, 11)]

with open("Tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
