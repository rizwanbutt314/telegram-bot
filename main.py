import telebot

from filters.private_chat import IsPrivateChat
from constants import BOT_TOKEN
from utils import (
    get_commands_function_mapping,
    get_query_handlers_function_mapping,
)

bot = telebot.TeleBot(BOT_TOKEN)


def register_filters():
    bot.add_custom_filter(IsPrivateChat())


def register_commands():
    """
    This function iterates over the folders in commands folder
    and will load the folders as command if it follows the 
    required structure.
    e.g.
    - start/ (folder name as command)
        - main.py:
            Required - This file should have function executor(message, bot)
        - handlers.py:
            Optional - If this file is present then it should have functions 
            query_handler(call, bot) and query_handler_filter(call)
        - menu.py:
            Optional - This contains the logic to generate the menu buttons for a command
        - messages.py:
            Optional - This contains the messages constants for a specific command
    """
    commands_fn_mapping = get_commands_function_mapping()

    for command, fn in commands_fn_mapping.items():
        bot.register_message_handler(fn, commands=[command], pass_bot=True)


def register_query_handlers():
    """
    This function iterates over the folders in commands folder
    and will load the handlers inside the folder if it follows the 
    required structure.
    e.g.
    - start/ (folder name as command)
        - handlers.py:
            Optional - If this file is present then it should have functions 
            query_handler(call, bot) and query_handler_filter(call)
    """
    handlers_fn_mapping = get_query_handlers_function_mapping()

    for _, fns in handlers_fn_mapping.items():
        query_handler_fn, query_handler_filter_fn = fns["query_handler"], fns["query_handler_filter"]

        bot.register_callback_query_handler(
            query_handler_fn, func=query_handler_filter_fn, pass_bot=True)


if __name__ == "__main__":
    # Register Filters
    register_filters()

    # Register Commands
    register_commands()

    # Register Query Handlers
    register_query_handlers()

    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers(delay=2)

    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()

    bot.infinity_polling()
