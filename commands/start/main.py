from .menu import start_command_menus


def executor(message, bot):
    bot.send_message(chat_id=message.chat.id,
                     text="Enter your activation code by selecting /activate. Once activated you would receive an email with detailed instructions.",
                     reply_markup=start_command_menus(),
                     parse_mode='HTML')
