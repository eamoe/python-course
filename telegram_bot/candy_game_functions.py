import random
import candy_game_constants


def toss_coin():
    if random.randint(0, 1) == 0:
        coin_side = 1
    else:
        coin_side = -1
    return coin_side


def print_first_move_player(first_move):
    first_move_message = ""
    match first_move:
        case 1:
            first_move_message = f"Поздравляю! {candy_game_constants.players[0]} делаешь первый ход!"
        case -1:
            first_move_message = f"Первый ход делает {candy_game_constants.players[1]}!"
    return first_move_message


def current_move(turn):
    if turn == -1:
        player = 2
    else:
        player = 1
    return player


def get_machine_take(remainder, max_take):
    if remainder > max_take:
        if remainder % max_take == 0 or remainder % max_take == 1:
            current_take = random.randint(1, max_take)
        else:
            current_take = remainder % max_take - 1
    else:
        current_take = remainder
    return current_take


def is_game_over(remainder, player):
    is_finished = 0
    game_over_message = ''
    if remainder <= 0:
        match player:
            case 1:
                game_over_message = f"Поздравляю с победой!"
                is_finished = 1
            case 2:
                game_over_message = f"Увы, это поражение!"
                is_finished = 1
    return [is_finished, game_over_message]


def flip_turn(turn):
    if turn == -1:
        turn = 1
    else:
        turn = -1
    return turn
