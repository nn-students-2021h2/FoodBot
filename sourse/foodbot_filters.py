"""
File containing the filter class needed to validate user input
"""
from telegram.ext import UpdateFilter


class FoodBotFilters(UpdateFilter):

    nutrients_count = 0
    nutrients_flag = 0

    def __init__(self, state):
        self.user_response = None
        self.state = state

    def filter(self, update):

        int_states = (
            "user_age",
            "user_height",
            "user_weight",
            "get_meal_size",
            "get_meal_calories",
            "get_meal_proteins",
            "get_meal_fats",
            "get_meal_carbs",
        )

        str_states = (
            "user_sex",
            "user_goal",
            "user_activity",
            "get_nutrients_norm",
            "get_statistic",
            "update_user_data",
            "add_new_meal",
            "delete_last_meal_note",
            "return_to_menu",
            "get_statistic_day",
            "get_statistic_week",
            "get_statistic_month",
            "update_name",
            "update_age",
            "update_sex",
            "update_height",
            "update_weight",
            "update_activity",
            "update_goal",
            "nutrients_recount",
        )
        correct_user_inputs = {
            "sex_types": ("мужской", "женский"),
            "activity_types": (
                "нулевая",
                "слабая",
                "средняя",
                "высокая",
                "экстремальная",
            ),
            "goal_types": ("похудение", "поддержание формы", "набор массы"),
        }

        correct_buttons = {
            "get_nutrients_norm": "вспомнить свою норму кбжу",
            "get_statistic": "получить статистику",
            "update_user_data": "изменить персональные данные",
            "add_new_meal": "внести прием пищи",
            "delete_last_meal_note": "удалить запись о последнем приеме пищи",
            "return_to_menu": "вернуться в основное меню",
            "update_name": "имя",
            "update_age": "возраст",
            "update_sex": "пол",
            "update_height": "рост",
            "update_weight": "вес",
            "update_activity": "уровень активности",
            "update_goal": "цель",
            "return_to_main_go": "вернуться в основное меню",
            "get_statistic_day": "за текущий день",
            "get_statistic_week": "за последние 7 дней",
            "get_statistic_month": "за последний месяц",
            "nutrients_recount": "пересчитать норму кбжу",
        }

        if self.state in int_states:
            try:
                self.user_response = float(update.message.text)
            except TypeError:
                update.message.reply_text(
                    "Я тебя не понимаю... Пожалуйста, введи целое число :)"
                )
            except ValueError:
                update.message.reply_text(
                    "Кажется, ты вводишь буквы или дробное число. "
                    "Пожалуйста, введи целое число."
                )
            else:
                if self.state == "user_age":
                    try:
                        if self.user_response < 16 or self.user_response > 99:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text(
                            "Бот предназначен для пользователей от 16 до 99 лет. "
                            "Если это опечатка, введи свой возраст еще раз."
                        )
                    else:
                        return True

                elif self.state == "user_height":
                    try:
                        if self.user_response < 100 or self.user_response > 300:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text(
                            "Кажется, у тебя опечатка... Пожалуйста, введи свой рост еще раз."
                        )
                    else:
                        return True

                elif self.state == "user_weight":
                    try:
                        if self.user_response not in range(20, 1000):
                            raise ValueError
                    except ValueError:
                        update.message.reply_text(
                            "Кажется, у тебя опечатка... Пожалуйста, введи свой вес еще раз."
                        )
                    else:
                        return True

                elif self.state == "get_meal_size":
                    try:
                        if self.user_response not in range(1, 2000):
                            raise ValueError
                    except ValueError:
                        update.message.reply_text(
                            "Кажется, у тебя опечатка... "
                            "Пожалуйста, введи размер порции еще раз."
                        )
                    else:
                        return True

                elif self.state == "get_meal_calories":
                    try:
                        # pad-thai is the world's most calorific dish (1004 kcal)
                        if self.user_response not in range(1, 1004):
                            raise ValueError
                    except ValueError:
                        update.message.reply_text(
                            "По моим данным, самое калорийное блюдо мира — лапша пад-тай "
                            "(1004 ккал/100г). Я ошибаюсь или у тебя опечатка? Попробуй ввести "
                            "калорийность еще раз."
                        )
                    else:
                        return True

                elif self.state in (
                    "get_meal_proteins",
                    "get_meal_fats",
                    "get_meal_carbs",
                ):
                    try:
                        if FoodBotFilters.nutrients_flag == 3:
                            FoodBotFilters.nutrients_count = 0
                            FoodBotFilters.nutrients_flag = 0
                        FoodBotFilters.nutrients_count += self.user_response
                        FoodBotFilters.nutrients_flag += 1
                        if (
                            self.user_response >= 100
                            or self.nutrients_count > 100
                            or self.user_response <= 0.01
                        ):
                            raise ValueError
                    except ValueError:
                        FoodBotFilters.nutrients_count -= self.user_response
                        update.message.reply_text(
                            "В 100 г продукта не может быть более 100 г и меньше 0.01"
                            " г нутриентов..."
                            "Пожалуйста, проверь, что ты вводишь БЖУ правильно "
                            "и попробуй еще раз."
                        )
                    else:
                        return True

        elif self.state in str_states:
            try:
                if not update.message.text:
                    raise ValueError
            except ValueError:
                update.message.reply_text(
                    "Я получил пустую строку... Пожалуйста, попробуй еще раз."
                )
            else:
                self.user_response = update.message.text

                if self.state == "user_sex":
                    if self.user_response.lower() in correct_user_inputs["sex_types"]:
                        return True
                    update.message.reply_text(
                        "Гендеров много, а полов всего два. "
                        "Какой пол у тебя: женский или мужской?"
                    )

                elif self.state == "user_activity":
                    if (
                        self.user_response.lower()
                        in correct_user_inputs["activity_types"]
                    ):
                        return True
                    update.message.reply_text(
                        "Такого уровня активности я не знаю... "
                        "Выбери наиболее подходящий тебе уровень на клавиатуре."
                    )

                elif self.state == "user_goal":
                    if self.user_response.lower() in correct_user_inputs["goal_types"]:
                        return True
                    update.message.reply_text(
                        "Такой цели я не знаю... "
                        "Выбери наиболее подходящую тебе цель на клавиатуре."
                    )

                elif self.state == "update_user_data":
                    if (
                        self.user_response.lower()
                        == correct_buttons["update_user_data"]
                    ):
                        return True

                elif self.state == "get_nutrients_norm":
                    if (
                        self.user_response.lower()
                        == correct_buttons["get_nutrients_norm"]
                    ):
                        return True

                elif self.state == "get_statistic":
                    if self.user_response.lower() == correct_buttons["get_statistic"]:
                        return True

                elif self.state == "add_new_meal":
                    if self.user_response.lower() == correct_buttons["add_new_meal"]:
                        return True

                elif self.state == "delete_last_meal_note":
                    if (
                        self.user_response.lower()
                        == correct_buttons["delete_last_meal_note"]
                    ):
                        return True

                elif self.state == "return_to_menu":
                    if self.user_response.lower() == correct_buttons["return_to_menu"]:
                        return True

                elif self.state == "get_statistic_day":
                    if (
                        self.user_response.lower()
                        == correct_buttons["get_statistic_day"]
                    ):
                        return True

                elif self.state == "get_statistic_week":
                    if (
                        self.user_response.lower()
                        == correct_buttons["get_statistic_week"]
                    ):
                        return True

                elif self.state == "get_statistic_month":
                    if (
                        self.user_response.lower()
                        == correct_buttons["get_statistic_month"]
                    ):
                        return True

                elif self.state == "nutrients_recount":
                    if (
                        self.user_response.lower()
                        == correct_buttons["nutrients_recount"]
                    ):
                        return True

                elif self.state == "update_name":
                    if self.user_response.lower() == correct_buttons["update_name"]:
                        return True

                elif self.state == "update_age":
                    if self.user_response.lower() == correct_buttons["update_age"]:
                        return True

                elif self.state == "update_sex":
                    if self.user_response.lower() == correct_buttons["update_sex"]:
                        return True

                elif self.state == "update_height":
                    if self.user_response.lower() == correct_buttons["update_height"]:
                        return True

                elif self.state == "update_weight":
                    if self.user_response.lower() == correct_buttons["update_weight"]:
                        return True

                elif self.state == "update_activity":
                    if self.user_response.lower() == correct_buttons["update_activity"]:
                        return True

                elif self.state == "update_goal":
                    if self.user_response.lower() == correct_buttons["update_goal"]:
                        return True

                elif self.state == "return_to_menu":
                    if self.user_response.lower() == correct_buttons["return_to_menu"]:
                        return True

        return False
