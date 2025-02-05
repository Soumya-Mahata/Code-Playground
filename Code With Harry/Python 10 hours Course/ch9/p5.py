words = ['sala', 'chutia', 'mc', 'harami']

with open("file.txt") as f:
    content = f.read()

for item in words:
    content = content.replace(item, "*" * len(item))

with open("file.txt", 'w') as f:
    f.write(content)