from telebot import types

FAQ_QUESTIONS = {
    "1": "Which cryptocurrencies does the service cover?",
    "2": "Can I try the service before I subscribe?",
    "3": "How often will I receive signals from the service?",
    "4": "Payments",
    "5": "Which Exchanges are compatible with the signals?",
    "6": "Do I need prior trading experience?",
    "7": "How are signals generated?",
    "8": "Why am I not receiving any signals?",
    "9": "How do I set up automation?",
    "10": "Detailed reports of trading histories?",
    "11": "Can I re-share/sell signals?",
    "12": "Will the service provide support and guidance on how to use the signals?",
    "13": "Will the service provide updates on market conditions and news?",
    "14": "What is a webhook API?",
    "15": "How much do I need to trade your signals?",
}


def faq_command_menus():
    markup = types.InlineKeyboardMarkup()

    for key, value in FAQ_QUESTIONS.items():
        markup.add(
            types.InlineKeyboardButton(text=value, callback_data=key)
        )

    return markup


def faq_command_back_menus():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text="Back", callback_data="faq-back")
    )

    return markup
