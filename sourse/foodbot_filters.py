from telegram.ext import UpdateFilter

nutrients_count = 0


class FoodBotFilters(UpdateFilter):

    def __init__(self, state):
        self.user_response = None
        self.state = state

    def filter(self, update):

        global nutrients_count

        int_states = ("user_age", "user_height", "user_weight", "get_meal_size", "get_meal_calories",
                      "get_meal_proteins", "get_meal_fats", "get_meal_carbs")

        str_states = ("user_sex", "user_goal", "user_activity", "get_nutrients_norm", "get_statistic",
                      "update_user_data", "add_new_meal", "delete_last_meal_note", "return_to_main_go",
                      "get_statistic_day", "get_statistic_week", "get_statistic_month", "update_name",
                      "update_age", "update_sex", "update_height", "update_weight", "update_activity",
                      "update_goal", "nutrients_recount")
        correct_user_inputs = {
            "sex_types": ("мужской", "женский"),
            "activity_types": ("нулевая", "слабая", "средняя", "высокая", "экстремальная"),
            "goal_types": ("похудение", "поддержание формы", "набор веса")
        }

        correct_buttons = {
            "get_nutrients_norm": "вспомнить свою норму кбжу",
            "get_statistic": "получить статистику",
            "update_user_data": "изменить персональные данные",
            "add_new_meal": "внести прием пищи",
            "delete_last_meal_note": "удалить запись о последнем приеме пищи",
            "return_to_main_go": "вернуться в основное меню",
            "update_name": "имя",
            "update_age": "возраст",
            "update_sex": "пол",
            "update_height": "рост",
            "update_weight": "вес",
            "update_activity": "уровень активности",
            "update_goal": "цель",
            "get_statistic_day": "за текущий день",
            "get_statistic_week": "за последние 7 дней",
            "get_statistic_month": "за последний месяц",
            "nutrients_recount": "пересчитать норму кбжу"
        }

        if self.state in int_states:
            try:
                self.user_response = int(update.message.text)
            except TypeError:
                update.message.reply_text("Вижу непонятно что, а надо цифры...")
            except ValueError:
                update.message.reply_text("Вижу буквы, а надо цифры...")
            else:
                if self.state == "user_age":
                    try:
                        if self.user_response < 16 or self.user_response > 99:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text("Неправильное значение возраста!")
                    else:
                        return True

                elif self.state == "user_height":
                    try:
                        if self.user_response not in range(100, 300):
                            raise ValueError
                    except ValueError:
                        update.message.reply_text("Неправильное значение роста!")
                    else:
                        return True

                elif self.state == "user_weight":
                    try:
                        if self.user_response > 1000:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text("Неправильное значение веса!")
                    else:
                        return True

                elif self.state == "get_meal_size":
                    try:
                        if self.user_response > 1000:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text("Неправильное значение массы!")
                    else:
                        return True

                elif self.state == "get_meal_calories":
                    try:
                        # pad-thai is the world's most calorific dish (1004 kcal)
                        if self.user_response > 1004:
                            raise ValueError
                    except ValueError:
                        update.message.reply_text("Неправильное значение калорийности!")
                    else:
                        return True

                elif self.state in ("get_meal_proteins", "get_meal_fats", "get_meal_carbs"):
                    try:
                        nutrients_count += self.user_response
                        if self.user_response >= 100 or nutrients_count > 100:
                            raise ValueError
                    except ValueError:
                        nutrients_count -= self.user_response
                        update.message.reply_text("В 100 г продукта не может быть более 100 г нутриентов..."
                                                  "Пожалуйста, проверьте корректность вводимых данных")
                    else:
                        return True

        elif self.state in str_states:
            try:
                if not update.message.text:
                    raise ValueError
            except ValueError:
                update.message.reply_text("Пустая строка?")
            else:
                self.user_response = update.message.text

                if self.state == "user_sex":
                    if self.user_response.lower() in correct_user_inputs["sex_types"]:
                        return True
                    update.message.reply_text(f"Неправильное значение пола!")

                elif self.state == "user_activity":
                    if self.user_response.lower() in correct_user_inputs["activity_types"]:
                        return True
                    update.message.reply_text(f"Неправильное значение активности!")

                elif self.state == "user_goal":
                    if self.user_response.lower() in correct_user_inputs["goal_types"]:
                        return True
                    update.message.reply_text(f"Неправильное значение цели!")

                elif self.state == "update_user_data":
                    if self.user_response.lower() == correct_buttons["update_user_data"]:
                        return True

                elif self.state == "get_nutrients_norm":
                    if self.user_response.lower() == correct_buttons["get_nutrients_norm"]:
                        return True

                elif self.state == "get_statistic":
                    if self.user_response.lower() == correct_buttons["get_statistic"]:
                        return True

                elif self.state == "add_new_meal":
                    if self.user_response.lower() == correct_buttons["add_new_meal"]:
                        return True

                elif self.state == "delete_last_meal_note":
                    if self.user_response.lower() == correct_buttons["delete_last_meal_note"]:
                        return True

                elif self.state == "return_to_main_go":
                    if self.user_response.lower() == correct_buttons["return_to_main_go"]:
                        return True

                elif self.state == "get_statistic_day":
                    if self.user_response.lower() == correct_buttons["get_statistic_day"]:
                        return True

                elif self.state == "get_statistic_week":
                    if self.user_response.lower() == correct_buttons["get_statistic_week"]:
                        return True

                elif self.state == "get_statistic_month":
                    if self.user_response.lower() == correct_buttons["get_statistic_month"]:
                        return True

                elif self.state == "nutrients_recount":
                    if self.user_response.lower() == correct_buttons["nutrients_recount"]:
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

                elif self.state == "return_to_main_go":
                    if self.user_response.lower() == correct_buttons["return_to_main_go"]:
                        return True

        return False
