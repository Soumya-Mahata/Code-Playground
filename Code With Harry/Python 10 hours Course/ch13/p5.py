from functools import reduce 
max_value = lambda x, y: x if x >= y else y
list = [1, 667, 660, 2, 3, 4, 5, 535, 76, 7, 8, 9, 10]
val = reduce (max_value, list)  
print(val)