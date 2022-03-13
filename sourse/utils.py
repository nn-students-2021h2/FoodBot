from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from user_class import user_from_dict
from user_database import get_user_object, get_all_user_info


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
        one_time_keyboard=True,
    )
    return keyboard


def sex_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup([["мужской", "женский"]], one_time_keyboard=True)
    return keyboard


def activity_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [["нулевая", "слабая", "средняя", "высокая", "экстремальная"]],
        one_time_keyboard=True,
    )
    return keyboard


def goal_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [["похудение", "поддержание формы", "набор массы"]], one_time_keyboard=True
    )
    return keyboard


def update_user_data_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [
            ["Имя", "Возраст", "Пол"],
            ["Вес", "Рост"],
            ["Уровень активности", "Цель", "Вернуться в основное меню"],
        ],
        one_time_keyboard=True,
    )
    return keyboard


def nutrients_norm_recount_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [["Пересчитать норму калорий"]], one_time_keyboard=True
    )
    return keyboard


def get_statistic_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        [
            ["За текущий день"],
            ["За последние 7 дней"],
            ["За последний месяц"],
        ],
        one_time_keyboard=True,
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
