## Welcome to my python based connect 4 terminal game
from numpy import random 

default_array = [[0 for x in range(5)] for y in range(5)]


def get_user_input():
    user_input = int(input('Enter column choice 1-5:' + '\n'))
    return user_input


def human_round():
    user_input = get_user_input()
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



human_round()
computer_round()
human_round()
computer_round()

print(default_array)