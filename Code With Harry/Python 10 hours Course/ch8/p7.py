list = ['Soumya', 'Arkajit', 'Tuhin', 'Soumyadeep', 'Sneha', 'Trinakshi']

def Strip(list, word):
    new_list = []
    for item in list:
        if not (item == word):
            new_list.append(item.strip(word))
    return new_list
     
print(Strip(list, 'a'))