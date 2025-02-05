#Write a program to greet all the person names stored in a list ‘list’ and which starts with S. 
list = ["Sneha", "Trinakshi", "Mal", "Tuhin", "Arkajit", "Soumya"]
for i in list:
    if i.startswith("S"):
        print(f"Good Morning {i}")