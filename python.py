def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


def choose_index():
    choice = 'Wrong'

    while choice not in ['0','1','2']:
        choice = input('Pick a position (0,1,2): ')
        if choice not in ['0','1','2']:
            print('Sorry, invalid choice')
    
    return int(choice)


def input_string(game_list, position):
    stringinput = input('Please enter a string to input on the selected index position: ')

    game_list[position] = stringinput

    return game_list

def playfurther():
    continueplay = 'BLANK'

    while continueplay not in ['Y','N']:
        continueplay = input('Do you want to continue playing? (Y, N): ')
        if continueplay not in ['Y','N']:
            print('Sorry, invalid choice')
    
    if continueplay == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)

    position = choose_index()

    input_string(game_list, position)

    display_game(game_list)

    game_on = playfurther()