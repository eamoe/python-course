# Создайте программу для игры в "Крестики-нолики".


from operator import is_
from sre_parse import State


initial_state = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def update_state(state, row, column, symbol):
    state[row][column] = symbol
    return state


def print_field(state):
    for row in state:
        print_str = ""
        for column in row:
            print_str += column + "\t"
        print(print_str)


def is_game_over(current_state):
    is_finished = False
    
    empty_count = 0
    for row in current_state:
        for column in row:
            if column == '*':
                empty_count += 1
    if empty_count == 0:
        is_finished = True
    
    if current_state[0][0] == current_state[0][1] == current_state[0][2] == 'x' or current_state[0][0] == current_state[0][1] == current_state[0][2] == 'o':
        is_finished = True
    elif current_state[1][0] == current_state[1][1] == current_state[1][2] == 'x' or current_state[1][0] == current_state[1][1] == current_state[1][2] == 'o':
        is_finished = True
    elif current_state[2][0] == current_state[2][1] == current_state[2][2] == 'x' or current_state[2][0] == current_state[2][1] == current_state[2][2] == 'o':
        is_finished = True
    elif current_state[0][0] == current_state[1][0] == current_state[2][0] == 'x' or current_state[0][0] == current_state[1][0] == current_state[2][0] == 'o':
        is_finished = True
    elif current_state[0][1] == current_state[1][1] == current_state[2][1] == 'x' or current_state[0][1] == current_state[1][1] == current_state[2][1] == 'o':
        is_finished = True
    elif current_state[0][2] == current_state[1][2] == current_state[2][2] == 'x' or current_state[0][2] == current_state[1][2] == current_state[2][2] == 'o':
        is_finished = True
    elif current_state[0][0] == current_state[1][1] == current_state[2][2] == 'x' or current_state[0][0] == current_state[1][1] == current_state[2][2] == 'o':
        is_finished = True
    elif current_state[2][0] == current_state[1][1] == current_state[0][2] == 'x' or current_state[2][0] == current_state[1][1] == current_state[0][2] == 'o':
        is_finished = True

    return is_finished
    

def get_move(player, symbol, state):
    check = False
    while not check:
        row = int(input(f"Игрок {player}, выберите строку: "))
        column = int(input(f"Игрок {player}, выберите столбец: "))
        if state[row][column] == 'x' or state[row][column] == 'o':
            print("Некорректный ход! Попробуйте снова!")
        else:
            check = True
    return (row, column)


def turn_move(player):
    if player == 1:
        return (2, 'o')
    else:
        return (1, 'x')

player = 2
symbol = 'o'
game_state = initial_state
print_field(game_state)

while not is_game_over(game_state):
    (player, symbol) = turn_move(player)
    (row, column) = get_move(player, symbol, game_state)
    game_state = update_state(game_state, row, column, symbol)
    print_field(game_state)

print("Игра окончена!")