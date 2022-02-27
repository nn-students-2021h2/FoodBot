from telegram import ReplyKeyboardMarkup


def initial_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup([["Познакомиться"]], resize_keyboard=True)
    return keyboard


def existing_user_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [
            ["Внести прием пищи"],
            ["Вспомнить свою норму КБЖУ"],
            ["Получить статистику"],
            ["Изменить персональные данные"],
            ["Удалить мой дневник"],
        ],
        resize_keyboard=True,
    )
    return keyboard
