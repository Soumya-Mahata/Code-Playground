import random

def game():
    print('You are playing the game...`')
    score = random.randint(1,100)
    print(f'Your score: {score}')
    return score

with open('Hi-Score.txt') as f:
    hiscore = f.read()
    if (hiscore != ''):
        hiscore = int(hiscore)
    else:
        hiscore = 0

score = game()
if (score > hiscore):
    with open('Hi-Score.txt', 'w') as f:
        f.write(str(score))