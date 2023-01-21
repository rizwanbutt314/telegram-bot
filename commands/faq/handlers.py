from .messages import FAQ_HEADER_MESSAGE, FAQ_ANSWERS
from .menu import faq_command_menus, faq_command_back_menus, FAQ_QUESTIONS
from .main import executor


def query_handler_filter(call): return call.data in FAQ_QUESTIONS.keys(
) or call.data == "faq-back" or call.data == "faq"


def query_handler(call, bot):
    _input = call.data

    if _input == "faq":
        executor(call.message, bot)
    elif _input == "faq-back":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              text=FAQ_HEADER_MESSAGE,
                              message_id=call.message.message_id,
                              reply_markup=faq_command_menus(),
                              parse_mode='HTML')
    else:
        answer = FAQ_ANSWERS.get(_input, "")

        bot.edit_message_text(chat_id=call.message.chat.id,
                              text=answer,
                              message_id=call.message.message_id,
                              reply_markup=faq_command_back_menus(),
                              parse_mode='HTML')
