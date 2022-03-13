import datetime
import pytz
import json
import handlers
from pathlib import Path
from jsonschema import validate
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters,
)
from utils import send_every_day_info
from foodbot_filters import FoodBotFilters


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
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("start", handlers.start)],
            states={
                "user_name": [MessageHandler(Filters.text, handlers.get_user_name)],
                "user_birth_date": [
                    MessageHandler(
                        FoodBotFilters("user_age"), handlers.get_user_birth_date
                    )
                ],
                "user_sex": [
                    MessageHandler(FoodBotFilters("user_sex"), handlers.get_user_sex)
                ],
                "user_height": [
                    MessageHandler(
                        FoodBotFilters("user_height"), handlers.get_user_height
                    )
                ],
                "user_weight": [
                    MessageHandler(
                        FoodBotFilters("user_weight"), handlers.get_user_weight
                    )
                ],
                "user_activity": [
                    MessageHandler(
                        FoodBotFilters("user_activity"), handlers.get_user_activity
                    )
                ],
                "user_goal": [
                    MessageHandler(FoodBotFilters("user_goal"), handlers.get_user_goal)
                ],
            },
            fallbacks=[],
        )
    )
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("go", handlers.go)],
            states={
                "main_go": [
                    MessageHandler(
                        FoodBotFilters("get_nutrients_norm"),
                        handlers.get_nutrients_norm,
                    ),
                    MessageHandler(
                        FoodBotFilters("get_statistic"), handlers.get_statistic
                    ),
                    MessageHandler(
                        FoodBotFilters("update_user_data"), handlers.update_user_data
                    ),
                    MessageHandler(
                        FoodBotFilters("add_new_meal"), handlers.add_new_meal
                    ),
                    MessageHandler(
                        FoodBotFilters("delete_last_meal_note"),
                        handlers.delete_last_meal_note,
                    ),
                ],
                "update_user_data": [
                    MessageHandler(
                        FoodBotFilters("update_name"), handlers.ask_for_new_user_name
                    ),
                    MessageHandler(
                        FoodBotFilters("update_age"), handlers.ask_for_new_user_age
                    ),
                    MessageHandler(
                        FoodBotFilters("update_sex"), handlers.ask_for_new_user_sex
                    ),
                    MessageHandler(
                        FoodBotFilters("update_height"),
                        handlers.ask_for_new_user_height,
                    ),
                    MessageHandler(
                        FoodBotFilters("update_weight"),
                        handlers.ask_for_new_user_weight,
                    ),
                    MessageHandler(
                        FoodBotFilters("update_activity"),
                        handlers.ask_for_new_user_activity,
                    ),
                    MessageHandler(
                        FoodBotFilters("update_goal"), handlers.ask_for_new_user_goal
                    ),
                    MessageHandler(FoodBotFilters("return_to_main_go"), handlers.go),
                ],
                "update_user_name": [
                    MessageHandler(Filters.text, handlers.update_user_name)
                ],
                "update_user_age": [
                    MessageHandler(FoodBotFilters("user_age"), handlers.update_user_age)
                ],
                "update_user_sex": [
                    MessageHandler(FoodBotFilters("user_sex"), handlers.update_user_sex)
                ],
                "update_user_height": [
                    MessageHandler(
                        FoodBotFilters("user_height"), handlers.update_user_height
                    )
                ],
                "update_user_weight": [
                    MessageHandler(
                        FoodBotFilters("user_weight"), handlers.update_user_weight
                    )
                ],
                "update_user_activity": [
                    MessageHandler(
                        FoodBotFilters("user_activity"), handlers.update_user_activity
                    )
                ],
                "update_user_goal": [
                    MessageHandler(
                        FoodBotFilters("user_goal"), handlers.update_user_goal
                    )
                ],
                "update_user_norm": [
                    MessageHandler(
                        FoodBotFilters("main_state"), handlers.update_user_norm
                    )
                ],
                "get_meal_name": [MessageHandler(Filters.text, handlers.get_meal_name)],
                "get_meal_size": [
                    MessageHandler(
                        FoodBotFilters("get_meal_size"), handlers.get_meal_size
                    )
                ],
                "get_meal_size_alternative": [
                    MessageHandler(
                        FoodBotFilters("get_meal_size"),
                        handlers.get_meal_size_alternative,
                    )
                ],
                "get_meal_calories": [
                    MessageHandler(
                        FoodBotFilters("get_meal_calories"), handlers.get_meal_calories
                    )
                ],
                "get_meal_proteins": [
                    MessageHandler(
                        FoodBotFilters("get_meal_proteins"), handlers.get_meal_proteins
                    )
                ],
                "get_meal_fats": [
                    MessageHandler(
                        FoodBotFilters("get_meal_fats"), handlers.get_meal_fats
                    )
                ],
                "get_meal_carbs": [
                    MessageHandler(
                        FoodBotFilters("get_meal_carbs"), handlers.get_meal_carbs
                    )
                ],
                "get_statistic_for": [
                    MessageHandler(
                        FoodBotFilters("get_statistic_day"),
                        handlers.get_statistic_for_day,
                    ),
                    MessageHandler(
                        FoodBotFilters("get_statistic_week"),
                        handlers.get_statistic_for_week,
                    ),
                    MessageHandler(
                        FoodBotFilters("get_statistic_month"),
                        handlers.get_statistic_for_month,
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
