from telegram import ReplyKeyboardMarkup, KeyboardButton


def keyboards():
    initial_keyboard = ReplyKeyboardMarkup([['Познакомиться']], resize_keyboard=True)
    return initial_keyboard


def existing_user_keyboard():
    keyboard = ReplyKeyboardMarkup(
        [
            ['Внести прием пищи'], ['Вспомнить свою норму КБЖУ'],
            ['Получить статистику'], ['Изменить персональные данные'],
            ['Удалить мой дневник']
        ], resize_keyboard=True)
    return keyboard
