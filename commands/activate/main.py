import telebot as _telebot


def executor(message, bot):
    msg = bot.send_message(chat_id=message.chat.id,
                           text="Please provide your activation code"
                           )

    bot.register_next_step_handler(
        msg, process_activation_code_step, bot_token=bot.token)


def process_activation_code_step(message, bot_token):
    _bot = _telebot.TeleBot(bot_token)
    try:
        chat_id = message.chat.id
        code = message.text
        _bot.send_message(chat_id, f"Code : {code}")
    except Exception as e:
        _bot.reply_to(message, 'oooops')
