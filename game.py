human_turn = input('Input human turn:')
computer_turn = input('Input computer turn:')

if human_turn == computer_turn:
    print('Draw!')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print('Humanity wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('People wins!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('You win!')
else:
    print('Machine are winning!')
