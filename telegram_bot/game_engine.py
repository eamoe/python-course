import messages
import rewrite_current_values as save_values
import candy_game_constants as cg_constants
import candy_game_functions

def run_game(user_message):
    output_str = messages.initial_move_response
    user_take = int(user_message)
    player = 1
    current_amount = int(save_values.get_current_values(cg_constants.path)[1])

    if current_amount <= 0:
        return messages.game_over

    max_take = save_values.get_current_values(cg_constants.path)[2]
    remaining_candies = current_amount - user_take

    if remaining_candies > 0:
        output_str = messages.remains_after_user_move(remaining_candies)

    game_result = candy_game_functions.is_game_over(remaining_candies, player)
    if game_result[0] == 1:
        output_str = output_str + "\n" + game_result[1]
        save_values.set_current_values(cg_constants.path, 1, remaining_candies, max_take)
    else:
        player = 2
        machine_take = candy_game_functions.get_machine_take(remaining_candies, int(max_take))
        if remaining_candies <= int(max_take):
            output_str = output_str + messages.machine_final_take_reply(machine_take)
        else:
            output_str = output_str + messages.machine_take_reply(machine_take)
        remaining_candies = remaining_candies - machine_take
        if remaining_candies > 0:
            output_str = output_str + messages.remains_after_machine_move(remaining_candies)

        game_result = candy_game_functions.is_game_over(remaining_candies, player)
        if game_result[0] == 1:
            output_str = output_str + "\n" + game_result[1]

        save_values.set_current_values(cg_constants.path, 1, remaining_candies, max_take)
    return output_str