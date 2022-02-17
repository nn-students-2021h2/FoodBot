import user_meal_database as umd
import datetime


class Meal:
    def __init__(
        self,
        user_id: int,
        meal_id: int,
        dish: str,
        meal_size: float,
        average_calories: float = 0,
        average_proteins: float = 0,
        average_fats: float = 0,
        average_carbohydrates: float = 0,
        date: str = None,
        time: str = None,
    ):
        self.user_id = user_id
        self.meal_id = meal_id
        self.dish = dish
        self.meal_size = meal_size
        self.average_calories = average_calories
        self.average_proteins = average_proteins
        self.average_fats = average_fats
        self.average_carbohydrates = average_carbohydrates
        self.date = get_current_date() if (date is None) else date
        self.time = get_current_time() if (time is None) else time

    def count_nutrients(self):
        """
        counts nutrition facts based on dish data stored in dish_database
        """
        pass

    def meal_to_database(self) -> None:
        umd.add_meal_note(
            self.user_id,
            self.meal_id,
            self.dish,
            self.meal_size,
            self.average_calories,
            self.average_proteins,
            self.average_fats,
            self.average_carbohydrates,
            self.date,
            self.time,
        )

    def get_short_meal_info(self) -> str:
        return (
            f"Ваше блюдо '{self.dish}' массой {self.meal_size} г. содержит:\n"
            f"{(self.average_calories/100) * self.meal_size} ккал,\n"
            f"{(self.average_proteins/100) * self.meal_size} г. белков,\n"
            f"{(self.average_fats/100) * self.meal_size} г. жиров,\n"
            f"{(self.average_carbohydrates/100) * self.meal_size} г. углеводов"
        )


def get_current_date() -> str:
    date = datetime.date.today()
    return str(date)


def get_current_time() -> str:
    time = datetime.datetime.now().time()
    return str(time)[:8]


def meal_from_dict(meal_data: dict) -> Meal:
    meal = Meal(
        user_id=meal_data["user_id"],
        meal_id=meal_data["meal_id"],
        dish=meal_data["meal_dish"],
        meal_size=meal_data["meal_size"],
        average_calories=meal_data["meal_average_calories"],
        average_proteins=meal_data["meal_average_proteins"],
        average_fats=meal_data["meal_average_fats"],
        average_carbohydrates=meal_data["meal_average_carbohydrates"],
        date=meal_data["meal_date"],
        time=meal_data["meal_time"],
    )
    return meal


if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
