import datetime
import pytz
import json
from pathlib import Path
from jsonschema import validate
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters,
)
from handlers import *
from utils import send_every_day_info


def main():
    schema = {
        "type": "object",
        "properties": {"TOKEN": {"type": "string", "minLenght": 46, "maxLenght": 46}},
        "additionalProperties": False,
    }
    token = json.load(open(Path(__file__).parent.parent.parent / "token.json"))
    validate(instance=token, schema=schema)

    bot = Updater(token=token["TOKEN"], use_context=True)
    dispatcher = bot.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex("Познакомиться"), acquaintance)],
            states={
                "user_name": [MessageHandler(Filters.text, get_user_name)],
                "user_birth_date": [MessageHandler(Filters.text, get_user_birth_date)],
                "user_sex": [
                    MessageHandler(Filters.regex("мужской|женский"), get_user_sex)
                ],
                "user_height": [MessageHandler(Filters.text, get_user_height)],
                "user_weight": [MessageHandler(Filters.text, get_user_weight)],
                "user_activity": [
                    MessageHandler(
                        Filters.regex("нулевая|слабая|средняя|высокая|экстремальная"),
                        get_user_activity,
                    )
                ],
                "user_goal": [
                    MessageHandler(
                        Filters.regex("похудение|поддержание формы|набор массы"),
                        get_user_goal,
                    )
                ],
            },
            fallbacks=[],
        )
    )
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex("Go"), existing_user),
                MessageHandler(Filters.regex("Начнем"), existing_user),
            ],
            states={
                "main_state": [
                    MessageHandler(Filters.regex("Продолжить"), existing_user),
                    MessageHandler(
                        Filters.regex("Вспомнить свою норму КБЖУ"), get_cpfc_norm
                    ),
                    MessageHandler(Filters.regex("Получить статистику"), get_statistic),
                    MessageHandler(
                        Filters.regex("Изменить персональные данные"),
                        update_existing_user_data,
                    ),
                    MessageHandler(Filters.regex("Внести прием пищи"), add_new_meal),
                    MessageHandler(
                        Filters.regex("Удалить запись о последнем приеме пищи"),
                        delete_last_meal_note,
                    ),
                ],
                "update_existing_user_data": [
                    MessageHandler(Filters.regex("Имя"), pre_update_exiting_user_name),
                    MessageHandler(
                        Filters.regex("Возраст"), pre_update_exiting_user_age
                    ),
                    MessageHandler(Filters.regex("Пол"), pre_update_exiting_user_sex),
                    MessageHandler(
                        Filters.regex("Рост"), pre_update_exiting_user_height
                    ),
                    MessageHandler(
                        Filters.regex("Вес"), pre_update_exiting_user_weight
                    ),
                    MessageHandler(
                        Filters.regex("Уровень активности"),
                        pre_update_exiting_user_activity,
                    ),
                    MessageHandler(Filters.regex("Цель"), pre_update_exiting_user_goal),
                    MessageHandler(
                        Filters.regex("Вернуться в основное меню"), return_to_main_state
                    ),
                ],
                "update_exiting_user_name": [
                    MessageHandler(Filters.text, update_exiting_user_name)
                ],
                "update_exiting_user_age": [
                    MessageHandler(Filters.text, update_exiting_user_age)
                ],
                "update_exiting_user_sex": [
                    MessageHandler(Filters.text, update_exiting_user_sex)
                ],
                "update_exiting_user_height": [
                    MessageHandler(Filters.text, update_exiting_user_height)
                ],
                "update_exiting_user_weight": [
                    MessageHandler(Filters.text, update_exiting_user_weight)
                ],
                "update_exiting_user_activity": [
                    MessageHandler(Filters.text, update_exiting_user_activity)
                ],
                "update_exiting_user_goal": [
                    MessageHandler(Filters.text, update_exiting_user_goal)
                ],
                "update_exiting_user_norm": [
                    MessageHandler(Filters.text, update_exiting_user_norm)
                ],
                "get_meal_dish": [MessageHandler(Filters.text, get_meal_dish)],
                "get_meal_size": [MessageHandler(Filters.text, get_meal_size)],
                "get_meal_size_alternative": [
                    MessageHandler(Filters.text, get_meal_size_alternative)
                ],
                "get_meal_calories": [MessageHandler(Filters.text, get_meal_calories)],
                "get_meal_proteins": [MessageHandler(Filters.text, get_meal_proteins)],
                "get_meal_fats": [MessageHandler(Filters.text, get_meal_fats)],
                "get_meal_carbohydrates": [
                    MessageHandler(Filters.text, get_meal_carbohydrates)
                ],
                "get_statistic_for": [
                    MessageHandler(
                        Filters.regex("За текущий день"), get_statistic_for_day
                    ),
                    MessageHandler(
                        Filters.regex("За последние 7 дней"), get_statistic_for_week
                    ),
                    MessageHandler(
                        Filters.regex("За последний месяц"), get_statistic_for_month
                    ),
                ],
            },
            fallbacks=[],
        )
    )

    bot.start_polling()

    bot.job_queue.run_daily(
        send_every_day_info,
        datetime.time(21, 0, 0, 0, tzinfo=pytz.timezone("Europe/Moscow")),
        days=(0, 1, 2, 3, 4, 5, 6),
    )

    bot.idle()


if __name__ == "__main__":
    main()
