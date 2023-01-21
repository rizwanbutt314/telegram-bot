from telebot import custom_filters, types


class IsPrivateChat(custom_filters.SimpleCustomFilter):
    # Class will only the bot to process if it's a private chat
    key = 'is_private_chat'

    @staticmethod
    def check(message: types.Message):
        return message.chat.type == "private"
