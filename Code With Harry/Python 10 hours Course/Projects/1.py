# PROJECT 1: STONE, PAPER, SCISSOR GAME 

from random import randint
bot = randint(1,3)

input = input(f'Choose among: Stone, Paper & Scissor \n\t\'a\' for Stone \n\t\'b\' for Paper \n\t\'c\' for Scissor \nType here: ')
input_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict = {1: 'Stone', 2: 'Paper', 3: 'Scissor'}

print(f'You chose: {reverse_dict[input_dict[input]]} \nComputer chose : {reverse_dict[bot]} \n')

if (bot == 1) and (input_dict[input] == 1):
    print('Its a Draw.')
elif (bot == 1) and (input_dict[input] == 2):
    print('You Win.')
elif (bot == 1) and (input_dict[input] == 3):
    print('You Loose.')

elif (bot == 2) and (input_dict[input] == 2):
    print('Its a Draw.')
elif (bot == 2) and (input_dict[input] == 3):
    print('You Win.')
elif (bot == 2) and (input_dict[input] == 1):
    print('You Loose.')
    
elif (bot == 3) and (input_dict[input] == 3):
    print('Its a Draw.')
elif (bot == 3) and (input_dict[input] == 1):
    print('You Win.')
elif (bot == 3) and (input_dict[input] == 2):
    print('You Loose.')
else:
    print('Something went wrong.')

print('Play Again....')