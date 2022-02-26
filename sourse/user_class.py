import meal_class as mc
from user_database import *


class User:
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
        carbohydrate_norm: int = 0,
    ):
        """Constructor"""
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
        self.carbohydrate_norm = carbohydrate_norm

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
        self.calorie_norm *= activity_cf[self.activity]

        PROTEIN_IN_KCAL, CARB_IN_KCAL, FAT_IN_KCAL = 4, 4, 9

        self.protein_norm = round(
            self.calorie_norm * goal_cf[self.goal][0] / PROTEIN_IN_KCAL
        )
        self.fat_norm = round(self.calorie_norm * goal_cf[self.goal][1] / FAT_IN_KCAL)
        self.carbohydrate_norm = round(
            self.calorie_norm * goal_cf[self.goal][2] / CARB_IN_KCAL
        )

    def user_to_database(self) -> None:
        add_note(
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
            self.carbohydrate_norm,
        )

    def get_short_info(self) -> str:
        return (
            f"{self.name.title()}, ваша дневная норма калорий — {self.calorie_norm} ккал. \n"
            f"Белки: {self.protein_norm} г. \n"
            f"Жиры: {self.fat_norm} г. \n"
            f"Углеводы: {self.carbohydrate_norm} г."
        )

    def get_meal_statistic_for_day(self) -> str:
        calculated_calories = round(mc.calculate_calories_for_day(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_day(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_day(self.user_id))
        calculated_carbohydrates = round(mc.calculate_carbohydrates_for_day(self.user_id))
        calories_balans = round(self.calorie_norm - calculated_calories)
        proteins_balans = round(self.protein_norm - calculated_proteins)
        fats_balans = round(self.fat_norm - calculated_fats)
        carbohydrates_balans = round(self.carbohydrate_norm - calculated_carbohydrates)
        return (
            f"{self.name.title()}, за день вами поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbohydrates} г. углеводов. \n"
            f"Для покрытия дневной нормы необходимо еще: \n"
            f"{calories_balans if calories_balans > 0 else 0} ккал. \n"
            f"{proteins_balans if proteins_balans > 0 else 0} г. белков \n"
            f"{fats_balans if fats_balans > 0 else 0} г. жиров \n"
            f"{carbohydrates_balans if carbohydrates_balans > 0 else 0} г. углеводов \n"
        )

    def get_meal_statistic_for_week(self) -> str:
        calculated_calories = round(mc.calculate_calories_for_week(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_week(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_week(self.user_id))
        calculated_carbohydrates = round(mc.calculate_carbohydrates_for_week(self.user_id))
        calories_balans = round(((self.calorie_norm * 7) - calculated_calories) / 7)
        proteins_balans = round(((self.protein_norm * 7) - calculated_proteins) / 7)
        fats_balans = round(((self.fat_norm * 7) - calculated_fats) / 7)
        carbohydrates_balans = round(((self.carbohydrate_norm * 7) - calculated_carbohydrates) / 7)
        return (
            f"{self.name.title()}, за неделю вами было поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbohydrates} г. углеводов. \n"
            f"Для покрытия нормы в среднем в день вам не хватало: \n"
            f"{calories_balans if calories_balans > 0 else 0} ккал. \n"
            f"{proteins_balans if proteins_balans > 0 else 0} г. белков \n"
            f"{fats_balans if fats_balans > 0 else 0} г. жиров \n"
            f"{carbohydrates_balans if carbohydrates_balans > 0 else 0} г. углеводов\n"
        )

    def get_meal_statistic_for_month(self) -> str:
        calculated_calories = round(mc.calculate_calories_for_month(self.user_id))
        calculated_proteins = round(mc.calculate_proteins_for_month(self.user_id))
        calculated_fats = round(mc.calculate_fats_for_month(self.user_id))
        calculated_carbohydrates = round(mc.calculate_carbohydrates_for_month(self.user_id))
        calories_balans = round(((self.calorie_norm * 31) - calculated_calories) / 31)
        proteins_balans = round(((self.protein_norm * 31) - calculated_proteins) / 31)
        fats_balans = round(((self.fat_norm * 31) - calculated_fats) / 31)
        carbohydrates_balans = round(((self.carbohydrate_norm * 31) - calculated_carbohydrates) / 31)
        return (
            f"{self.name.title()}, за месяц вами было поглащено {calculated_calories} ккал. \n"
            f"{calculated_proteins} г. белков, \n"
            f"{calculated_fats} г. жиров, \n"
            f"{calculated_carbohydrates} г. углеводов. \n"
            f"Для покрытия нормы в среднем в день вам не хватало: \n"
            f"{calories_balans if calories_balans > 0 else 0} ккал. \n"
            f"{proteins_balans if proteins_balans > 0 else 0} г. белков \n"
            f"{fats_balans if fats_balans > 0 else 0} г. жиров \n"
            f"{carbohydrates_balans if carbohydrates_balans > 0 else 0} г. углеводов\n"
        )


def user_from_dict(user_data: dict) -> User:
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
        carbohydrate_norm=user_data["user_carbohydrate_norm"],
    )
    return user
