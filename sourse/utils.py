from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from user_class import user_from_dict
from user_database import get_user_object, get_all_user_info


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
            ["Удалить запись о последнем приеме пищи"],
        ],
        resize_keyboard=True,
    )
    return keyboard


def send_every_day_info(context: CallbackContext) -> None:
    all_data = get_all_user_info()
    for i in all_data:
        user = user_from_dict(get_user_object(all_data[i]["user_id"]))
        context.bot.send_message(
            chat_id=user.user_id, text=user.get_meal_statistic_for_day()
        )


if __name__ == "__main__":
    print(1)
