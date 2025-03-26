import random

def playercharacter():
    marker = ''
    while marker not in ['O','X']:
        marker = input('Player 1, please select a marker: (O or X) ')
        
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'

    return player1, player2


def displayboard(board):
    print('\n' * 2)
    print(board[1] + '\t|' + board[2] + '\t|' + board[3])
    print(board[4] + '\t|' + board[5] + '\t|' + board[6])
    print(board[7] + '\t|' + board[8] + '\t|' + board[9])


def check_winner(board, marker):
    for row in range(1, 8, 3):
        if board[row] == board[row + 1] == board[row + 2] == marker:
            return True
    
    for col in range(1, 4):
        if board[col] == board[col + 3] == board[col + 6] == marker:
            return True
        
    if board[1] == board[5] == board[9] == marker or board[3] == board[5] == board[7] == marker:
        return True
    
    return False


def reset_game():
    return ['#', '', '', '', '', '', '', '', '', ''], 1, 1


def index_choice(board, current_player):
    while True:
        choice = input(f'Player {current_player}, please pick a digit in position (1-9): ')
        if choice.isdigit() and int(choice) in range(1, 10):
            if board[int(choice)] == '':
                return int(choice)
            else:
                print(f'Player {current_player}: This position is already taken!')
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def aichoice(board):
    choice = random.randrange(1, 10)
    while board[choice] != '':
        choice = random.randrange(1, 10)
    return choice


def play_game():
    current_board, playercounter, current_player = reset_game()

    player1marker, player2marker = playercharacter()

    while '' in current_board:
        if playercounter % 2 != 0:
            current_player = 1
            chosenindex = index_choice(current_board, current_player)
            current_board[chosenindex] = player1marker
            displayboard(current_board)

            if check_winner(current_board, player1marker):
                print("Player 1 wins!\n\nThis TicTacToe session has been powered by Dentsu Merkury for Kids © 2025 Merkury")
                break

            playercounter += 1

        else:
            current_player = 2
            chosenindex = aichoice(current_board)
            current_board[chosenindex] = player2marker
            displayboard(current_board)

            if check_winner(current_board, player2marker):
                print("Player 2 wins!\n\nThis TicTacToe session has been powered by Dentsu Merkury for Kids © 2025 Merkury")
                break

            playercounter += 1

    play_again = input("Thank you for playing.\nDo you want to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        play_game()


play_game()