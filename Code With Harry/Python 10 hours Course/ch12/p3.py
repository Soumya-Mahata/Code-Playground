user_input = int(input("Enter a number: "))
list_comprehension = [(i * user_input) for i in range(1, 11)]
print(list_comprehension)