with open("log.txt") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if ("python" in line):
        print(f"Yes, Python is present in {line_no}-no line.")
        break
    line_no += 1
    
else:
    print("No, Python is not present.")