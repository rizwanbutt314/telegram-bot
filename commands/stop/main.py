from .messages import STOP_MSG

def executor(message, bot):
    bot.send_message(chat_id=message.chat.id,
                     text=STOP_MSG
                     )