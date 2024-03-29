import time

import api_keys as keys
from telegram.ext import *
import responses as responses
import org_menu


print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Организация'.upper())


def help_command(update, context):
    update.message.reply_text('If you need help, you should ask for it on Google!')


def org_command(update, context):
    update.message.reply_text(org_menu.show_menu())


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
    dp.add_handler(CommandHandler("Organization", org_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
