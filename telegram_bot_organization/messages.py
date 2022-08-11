play_command_response = 'Хорошо, давай поиграем!'

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
