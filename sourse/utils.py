from telegram import ReplyKeyboardMarkup, KeyboardButton


def keyboards():
    initial_keyboard = ReplyKeyboardMarkup([['Познакомиться']], resize_keyboard=True)
    return initial_keyboard
