from .messages import FAQ_HEADER_MESSAGE
from .menu import faq_command_menus

def executor(message, bot):
    bot.send_message(chat_id=message.chat.id,
                     text=FAQ_HEADER_MESSAGE,
                     reply_markup=faq_command_menus(),
                     parse_mode='HTML')