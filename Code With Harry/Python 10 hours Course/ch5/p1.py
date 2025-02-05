a = {'Arigato':'Thanks', 
     'Gomen':'Sorry', 
     'Gohan':'Rice', 
     'Konnichiwa':'Hello'}
b = input('Enter the JAP Word (Arigato, Gomen, Gohan, Konnichiwa): \n')
print(f' ENG meaning: {a.get(b)}')