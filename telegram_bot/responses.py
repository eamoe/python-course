from datetime import datetime

import candy_game_constants as cg_constants
import game_engine


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi'):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I'm an Eugene's bot!"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if int(user_message) in range(cg_constants.min_take, cg_constants.max_take + 1):
        return game_engine.run_game(user_message)

    if int(user_message) > 28 or int(user_message) < 0:
        return "Допустимые значения от 1 до 28!"

    return "I don't understand you!"
