#Assignment 1: Tic Tac Toe
# Author: Wylee Everett
stop = 'N'

def player_1_turn():
    repeat = True
    while repeat:
        selection = int(input('Player-1 Selection: '))
        if selection in open_squares:
            player_1_squares.append(selection)
            open_squares.remove(selection)
            repeat = False
        elif selection in player_1_squares:
            print('You have already claimed that space')
        elif selection in player_2_squares:
            print('Your opponent has already claimed that space')
        else:
            print('Make sure your selection is a number')

def player_2_turn():
    repeat = True
    while repeat:
        selection = int(input('Player-2 Selection: '))
        if selection in open_squares:
            player_2_squares.append(selection)
            open_squares.remove(selection)
            repeat = False
        elif selection in player_2_squares:
            print('You have already claimed that space')
        elif selection in player_1_squares:
            print('Your opponent has already claimed that space')
        else:
            print('Make sure your selection is a number')

def assemble_board():
    assembly = []
    for i in range(1,10):
        if i in open_squares:
            assembly.append(i)
        elif i in player_1_squares:
            assembly.append('x')
        elif i in player_2_squares:
            assembly.append('o')
        else:
            assembly.append('board assembly error')
    print(f' {assembly[0]} | {assembly[1]} | {assembly[2]} \n___________\n {assembly[3]} | {assembly[4]} | {assembly[5]} \n___________\n {assembly[6]} | {assembly[7]} | {assembly[8]} ')

def check_winner():
    if 1 in player_1_squares and 2 in player_1_squares and 3 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 4 in player_1_squares and 5 in player_1_squares and 6 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 7 in player_1_squares and 8 in player_1_squares and 9 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 1 in player_1_squares and 4 in player_1_squares and 7 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 2 in player_1_squares and 5 in player_1_squares and 8 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 3 in player_1_squares and 6 in player_1_squares and 9 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 1 in player_1_squares and 5 in player_1_squares and 9 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 3 in player_1_squares and 5 in player_1_squares and 7 in player_1_squares:
        winner = 1
        print('Player-1 Wins')
    elif 1 in player_2_squares and 2 in player_2_squares and 3 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 4 in player_2_squares and 5 in player_2_squares and 6 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 7 in player_2_squares and 8 in player_2_squares and 9 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 1 in player_2_squares and 4 in player_2_squares and 7 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 2 in player_2_squares and 5 in player_2_squares and 8 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 3 in player_2_squares and 6 in player_2_squares and 9 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 1 in player_2_squares and 5 in player_2_squares and 9 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif 3 in player_2_squares and 5 in player_2_squares and 7 in player_2_squares:
        winner = 1
        print('Player-2 Wins')
    elif len(open_squares) == 0:
        winner = 1
        print('Tie Game')
    else:
        winner = 0
    return winner

def main():
    assemble_board()
    winner = 0
    while winner == 0:
        player_1_turn()
        assemble_board()
        winner = check_winner()
        if winner == 1:
            break
        player_2_turn()
        assemble_board()
        winner = check_winner()
        if winner == 1:
            break

while stop == 'N':
    open_squares = [1,2,3,4,5,6,7,8,9]
    player_1_squares =[]
    player_2_squares =[]
    main()
    repeat2 = True
    while repeat2:
        stop = input('Would you like to quit?(Y/N): ').capitalize()
        if stop == 'Y':
            print('Thanks for playing!')
            repeat2 = False
        elif stop == 'N':
            repeat2 = False
        else:
            print(' Please use Y or N')