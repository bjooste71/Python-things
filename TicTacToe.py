current_board = ['#','','','','','','','','','']
current_player = 1



def playercharacter():
    marker = ''

    while marker != 'O' and  marker != 'X':
        marker = input('Player 1, please select a marker: ')
        
    
    player1 = marker

    if player1 == 'X':
        player2 == 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def displayboard(board):
    print('\n' *100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

displayboard(current_board)

def index_choice():
    choice = 'null'

    while not choice.isdigit():
        choice = input(f'Player {current_player}, please pick a position (1-9): ')
        print('Sorry, it must be a digit in position 1-9')


    while int(choice) not in range(1,10):
        choice = input(f'Player {current_player}, please pick a position (1-9): ')
        print('Sorry, it must be a digit in position 1-9')
    
    return int(choice)



