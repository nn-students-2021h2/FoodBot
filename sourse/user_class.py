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
        self.calorie_norm = 0
        self.protein_norm = 0
        self.fat_norm = 0
        self.carbohydrate_norm = 0

    def count_norm(self) -> None:
        """
        Counts daily norm of nutrients according to user's attributes
        Source: https://edatop.ru/252-raschet-bzhu.html#hmenu-10
        """

        activity_cf = {
            "Нулевая": 1.2,
            "Слабая": 1.375,
            "Средняя": 1.55,
            "Высокая": 1.7,
            "Экстремальная": 1.9,
        }

        # (proteins, fats, carbs) aka (б, ж, у)
        goal_cf = {
            "Поддержание формы": (0.3, 0.3, 0.4),
            "Похудение": (0.25, 0.25, 0.5),
            "Набор массы": (0.35, 0.3, 0.55),
        }

        if self.sex == "Женский":
            self.calorie_norm = round(
                447.6 + 9.2 * self.weight + 3.1 * self.height - 4.3 * self.age
            )
        elif self.sex == "Мужской":
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
