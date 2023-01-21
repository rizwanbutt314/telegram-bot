from .messages import FREE_INTRO_MSG

def executor(message, bot):
    bot.send_message(chat_id=message.chat.id,
                     text=FREE_INTRO_MSG
                     )