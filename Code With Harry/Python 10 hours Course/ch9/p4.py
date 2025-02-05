word = "Donkey"
new_word = "######"

with open("file.txt") as f:
    content = f.read()

new_content = content.replace(word, new_word)

with open("file.txt", 'w') as f:
    f.write(new_content)