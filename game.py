import random
turns = ['rock','paper','scissors']

while(True):
    human_turn = input('Enter your turn, or type exit:')
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thanks for playing!')
        break

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')

    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Humanity wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Humanity wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('You win!')
    else:
        print('Machine are winning!')
