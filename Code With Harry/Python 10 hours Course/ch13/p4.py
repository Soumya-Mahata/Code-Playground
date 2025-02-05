numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
function = lambda x: True if x % 5 == 0 else False
filtered_list = filter(function, numbers)
print(list(filtered_list))