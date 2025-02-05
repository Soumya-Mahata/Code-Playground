# PROJECT 2 – THE PERFECT GUESS GAME

import random
number = random.randint(1, 50)

n = 5
for i in range(1, n+1):
    user_input = int(input('Guess the number between 1 to 50: '))

    if (number == user_input):
        print(f'Game Over...You win. \nYou perfectly guessed the number in {i}th attempt.')
        break
    elif (number < user_input) and i != n:
        print(f'You entered a greater number, try with some smaller number. \nNo of turns left: {n - i} \n')
    elif (number > user_input) and i != n:
        print(f'You entered a smaller number, try with some greater number. \nNo of turns left: {n - i} \n')
else:
    print('Game Over...You lose. \nYou have run out of turns.')

print(f'The number was {number}')