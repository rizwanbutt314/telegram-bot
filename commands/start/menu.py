from telebot import types


def start_command_menus():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        text="Plans", url="https://core.telegram.org/bots/api#inlinekeyboardbutton"))
    markup.add(types.InlineKeyboardButton(
        text="Activate Plan", callback_data="activate"))
    markup.add(types.InlineKeyboardButton(text="FAQ", callback_data="faq"))

    return markup
