import time

import candy_game_constants
import api_keys as keys
from telegram.ext import *
import responses as responses
import messages
import candy_game_functions as cgf
import rewrite_current_values

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need help, you should ask for it on Google!')


def play_command(update, context):
    # Explain game rules
    update.message.reply_text(messages.play_command_response)
    time.sleep(2)
    update.message.reply_text(messages.candy_game_rules)

    # Get initial game settings and write them to file
    time.sleep(5)
    who_starts = 1
    update.message.reply_text(cgf.print_first_move_player(who_starts))
    initial_candies_number = candy_game_constants.candies_number
    max_take = candy_game_constants.max_take
    rewrite_current_values.set_current_values(candy_game_constants.path,
                                              who_starts,
                                              initial_candies_number,
                                              max_take)


def org_command(update, context):
    update.message.reply_text('Organization database!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Help", help_command))
    dp.add_handler(CommandHandler("Play", play_command))
    dp.add_handler(CommandHandler("Organization", org_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
