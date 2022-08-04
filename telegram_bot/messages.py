import candy_game_constants

play_command_response = 'Хорошо, давай поиграем!'

candy_game_rules = f'На столе лежит {candy_game_constants.candies_number} конфет.\n' + \
                   f'{candy_game_constants.players[0]} и я ' + \
                   f'по очереди будем брать несколько конфет - больше 1, ' + \
                   f'но меньше {candy_game_constants.max_take}. ' + \
                   'Победит тот, кто сделает последний ход. Он заберет все конфеты!'

initial_move_response = ""

game_over = "Игра окончена! Чтобы начать снова, нажми /play"


def remains_after_user_move(amount):
    return f"\nОсталось конфет: {amount}"


def remains_after_machine_move(amount):
    return f"остается {amount}. Твой ход!"


def machine_final_take_reply(amount):
    return f"\nЯ возьму оставшиеся {amount}. "


def machine_take_reply(amount):
    return f"\nЯ возьму {amount}, "
