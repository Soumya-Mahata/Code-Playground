with open('poems.txt') as f:
    content = f.read()
    if 'Twinkle' in content:
        print("Twinkle is Present.")
    else:
        print("Twinkle is not Present.")

