## Welcome to my python based connect 4 terminal game
from numpy import random 

default_array = [[0 for x in range(5)] for y in range(5)]

def get_user_input():
    user_input = int(input('Enter column choice 1-5:' + '\n'))
    return user_input


def human_round():
    print('\n')
    user_input = get_user_input()
    if user_input not in range(1,6):
        print("Enter valid number")
        human_round()

    for i in range(5):
        if i == user_input -1:
            for x in range(5):
                if default_array[4-x][i] == 0:
                    default_array[4-x][i] = 1
                    return
            print('This column is full,try again')
            return human_round()


def computer_round():
    column_choice_idx = random.randint(0,5)
    print(column_choice_idx)

    if default_array[1][column_choice_idx] == 0:
        for x in range(5):
            if default_array[4-x][column_choice_idx] == 0:
                default_array[4-x][column_choice_idx] = 2
                return
    else: 
        computer_round()

def check_for_winner():
    ## check rows
    for row_idx in range(5):
        row_to_check = default_array[row_idx]
        print(row_to_check)
        for start_idx in range(2):
            if row_to_check[start_idx:4+start_idx] == [1 for x in range(4)]:
                return 'Congratulations, you won!'
            
            if row_to_check[start_idx:4+start_idx] == [2 for x in range(4)]:
                return 'Oh no! The computer won'
            
    ##check columns
    for column_idx in range(5):
        column_to_check = [default_array[x][column_idx] for x in range(5)]
        
        for start_idx in range(2):
            if column_to_check[start_idx:4+start_idx] == [1 for x in range(4)]:
                return 'Congratulations, you won!'
            
            if column_to_check[start_idx:4+start_idx] == [2 for x in range(4)]:
                return 'Oh no! The computer won'            

            
    ##checking the 6 diagonals
    diag1 = [default_array[i][i] for i in range(5)]
    diag2 = [default_array[i][4-i] for i in range(5)]

    diag3 = [default_array[4-i][i+1] for i in range(4)]
    diag4 = [default_array[3-i][i] for i in range(4)]

    diag5 = [default_array[i+1][i] for i in range(4)]
    diag6 = [default_array[i][i+1] for i in range(4)]


    ## check longer diagonals
    for start_idx in range(2):
        if diag1[start_idx:4+start_idx] == [1 for x in range(4)]: 
            return 'Congratulations, you won!'
    
        if diag2[start_idx:4+start_idx] == [1 for x in range(4)]: 
            return 'Congratulations, you won!'    

        if diag1[start_idx:4+start_idx] == [2 for x in range(4)]: 
            return 'Oh no! The computer won'
    
        if diag2[start_idx:4+start_idx] == [2 for x in range(4)]: 
            return 'Oh no! The computer won'
        
    ## check shorter diagonals
    if diag3 == [1 for x in range(4)] or diag4 == [1 for x in range(4)] or diag5 == [1 for x in range(4)] or diag6 == [1 for x in range(4)]:
        return 'Congratulations, you won!'

    if diag3 == [2 for x in range(4)] or diag4 == [2 for x in range(4)] or diag5 == [2 for x in range(4)] or diag6 == [2 for x in range(4)]:
        return 'Oh no! The computer won'
            
    return False


print('Welcome to connect 4 played in the terminal, your pieces will be represented by 1 and the computer\'s by 2, get 4 in a row to win!')

print('\n')
print('Starting Board:')

game_finished = False

for row_idx in range(5):
        print(default_array[row_idx])

while game_finished == False:
    human_round()
    game_finished = check_for_winner()
    if game_finished == False:
        computer_round()
        game_finished = check_for_winner()

    print('\n')
    print('Current state:')
    for row_idx in range(5):
        print(default_array[row_idx])

    if game_finished != False:
        print(game_finished)





