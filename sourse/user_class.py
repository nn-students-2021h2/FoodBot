import meal_class as mc
import user_database as ud


class User:
    """
    Auxiliary class that contains information about the norm of nutrients and
    allows you to add a user to the database
    """

    def __init__(
        self,
        user_id: int,
        name: str,
        age: int,
        sex: str,
        height: int,
        weight: int,
        activity: str,
        goal: str,
        calorie_norm: int = 0,
        protein_norm: int = 0,
        fat_norm: int = 0,
        carb_norm: int = 0,
    ):
        self.user_id = user_id
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.height = int(height)
        self.weight = int(weight)
        self.activity = activity
        self.goal = goal
        self.calorie_norm = calorie_norm
        self.protein_norm = protein_norm
        self.fat_norm = fat_norm
        self.carb_norm = carb_norm

    def count_norm(self) -> None:
        """
        Counts daily norm of nutrients according to user's attributes
        Source: https://edatop.ru/252-raschet-bzhu.html#hmenu-10
        """

        activity_cf = {
            "нулевая": 1.2,
            "слабая": 1.375,
            "средняя": 1.55,
            "высокая": 1.7,
            "экстремальная": 1.9,
        }

        # (proteins, fats, carbs) aka (б, ж, у)
        goal_cf = {
            "поддержание формы": (0.3, 0.3, 0.4),
            "похудение": (0.25, 0.25, 0.5),
            "набор массы": (0.35, 0.3, 0.55),
        }

        if self.sex == "женский":
            self.calorie_norm = round(
                447.6 + 9.2 * self.weight + 3.1 * self.height - 4.3 * self.age
            )
        elif self.sex == "мужской":
            self.calorie_norm = round(
                88.36 + 13.4 * self.weight + 4.8 * self.height - 5.7 * self.age
            )
        self.calorie_norm *= activity_cf[self.activity.lower()]

        PROTEIN_IN_KCAL, CARB_IN_KCAL, FAT_IN_KCAL = 4, 4, 9

        self.protein_norm = round(self.calorie_norm * goal_cf[self.goal.lower()][0] / PROTEIN_IN_KCAL)
        self.fat_norm = round(self.calorie_norm * goal_cf[self.goal.lower()][1] / FAT_IN_KCAL)
        self.carb_norm = round(self.calorie_norm * goal_cf[self.goal.lower()][2] / CARB_IN_KCAL)

    def user_to_database(self) -> None:
        """
        Adds a user class object to the user database
        """
        ud.add_note(
            self.user_id,
            self.name,
            self.age,
            self.sex,
            self.height,
            self.weight,
            self.activity,
            self.goal,
            self.calorie_norm,
            self.protein_norm,
            self.fat_norm,
            self.carb_norm,
        )

    def get_short_info(self) -> str:
        """
        Returns a message with a summary of daily calories and nutrients
        """
        return (
            f"{self.name.title()}, ваша дневная норма калорий — {self.calorie_norm} ккал. \n"
            f"Белки: {self.protein_norm} г. \n"
            f"Жиры: {self.fat_norm} г. \n"
            f"Углеводы: {self.carb_norm} г."
        )

    def get_meal_statistic_for_day(self) -> str:
        """
        Returns message with user statistic for 1 day
        """
        calculated_calories = round(mc.calculate_calories_for_day(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_day(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_day(self.user_id))
        calculated_carbs = round(mc.calculate_carbs_for_day(self.user_id))
        calories_balance = round(self.calorie_norm - calculated_calories)
        proteins_balance = round(self.protein_norm - calculated_proteins)
        fats_balance = round(self.fat_norm - calculated_fats)
        carbs_balance = round(self.carb_norm - calculated_carbs)
        return (
            f"{self.name.title()}, за день вами поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbs} г. углеводов. \n"
            f"Для покрытия дневной нормы необходимо еще: \n"
            f"{calories_balance if calories_balance > 0 else 0} ккал. \n"
            f"{proteins_balance if proteins_balance > 0 else 0} г. белков \n"
            f"{fats_balance if fats_balance > 0 else 0} г. жиров \n"
            f"{carbs_balance if carbs_balance > 0 else 0} г. углеводов \n"
        )

    def get_meal_statistic_for_week(self) -> str:
        """
        Returns message with user statistic for last 7 days
        """
        calculated_calories = round(mc.calculate_calories_for_week(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_week(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_week(self.user_id))
        calculated_carbs = round(
            mc.calculate_carbs_for_week(self.user_id)
        )
        calories_balance = round(((self.calorie_norm * 7) - calculated_calories) / 7)
        proteins_balance = round(((self.protein_norm * 7) - calculated_proteins) / 7)
        fats_balance = round(((self.fat_norm * 7) - calculated_fats) / 7)
        carbs_balance = round(((self.carb_norm * 7) - calculated_carbs) / 7)
        return (
            f"{self.name.title()}, за неделю вами было поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbs} г. углеводов. \n"
            f"Для покрытия нормы в среднем в день вам не хватало: \n"
            f"{calories_balance if calories_balance > 0 else 0} ккал. \n"
            f"{proteins_balance if proteins_balance > 0 else 0} г. белков \n"
            f"{fats_balance if fats_balance > 0 else 0} г. жиров \n"
            f"{carbs_balance if carbs_balance > 0 else 0} г. углеводов\n"
        )

    def get_meal_statistic_for_month(self) -> str:
        """
        Returns message with user statistic for last 31 days
        """
        calculated_calories = round(mc.calculate_calories_for_month(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_month(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_month(self.user_id))
        calculated_carbs = round(mc.calculate_carbs_for_month(self.user_id))
        calories_balance = round(((self.calorie_norm * 31) - calculated_calories) / 31)
        proteins_balance = round(((self.protein_norm * 31) - calculated_proteins) / 31)
        fats_balance = round(((self.fat_norm * 31) - calculated_fats) / 31)
        carbs_balance = round(((self.carb_norm * 31) - calculated_carbs) / 31)
        return (
            f"{self.name.title()}, за месяц вами было поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbs} г. углеводов. \n"
            f"Для покрытия нормы в среднем в день вам не хватало: \n"
            f"{calories_balance if calories_balance > 0 else 0} ккал. \n"
            f"{proteins_balance if proteins_balance > 0 else 0} г. белков \n"
            f"{fats_balance if fats_balance > 0 else 0} г. жиров \n"
            f"{carbs_balance if carbs_balance > 0 else 0} г. углеводов\n"
        )


def user_from_dict(user_data: dict) -> User:
    """
    Returns user object created from user database data
    """
    user = User(
        user_id=user_data["user_id"],
        name=user_data["user_name"],
        age=user_data["user_age"],
        sex=user_data["user_sex"],
        height=user_data["user_height"],
        weight=user_data["user_weight"],
        activity=user_data["user_activity"],
        goal=user_data["user_goal"],
        calorie_norm=user_data["user_calorie_norm"],
        protein_norm=user_data["user_protein_norm"],
        fat_norm=user_data["user_fat_norm"],
        carb_norm=user_data["user_carb_norm"],
    )
    return user
