"""
File containing the implementation of the meal class and its accompanying functions
"""
import user_meal_database as umd
import datetime


class Meal:
    """
    Auxiliary class that stores information necessary for
    issuing to the user and adding to the meal database
    """

    def __init__(
        self,
        user_id: int,
        meal_id: int,
        dish: str,
        meal_size: float,
        average_calories: float = 0,
        average_proteins: float = 0,
        average_fats: float = 0,
        average_carbs: float = 0,
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
        self.average_carbs = average_carbs
        self.date = get_current_date() if (date is None) else date
        self.time = get_current_time() if (time is None) else time

    def meal_to_database(self) -> None:
        """
        Adds a meal class object to the meal database
        """
        umd.add_meal_note(
            self.user_id,
            self.meal_id,
            self.dish,
            self.meal_size,
            self.average_calories,
            self.average_proteins,
            self.average_fats,
            self.average_carbs,
            self.date,
            self.time,
        )

    def get_short_meal_info(self) -> str:
        """
        Returns message with a summary of the nutritional value of a meal
        """
        return (
            f"Ваше блюдо '{self.dish}' массой {round(self.meal_size)} г. содержит:\n"
            f"{round((self.average_calories/100) * self.meal_size)} ккал,\n"
            f"{round((self.average_proteins/100) * self.meal_size)} г. белков,\n"
            f"{round((self.average_fats/100) * self.meal_size)} г. жиров,\n"
            f"{round((self.average_carbs/100) * self.meal_size)} г. углеводов"
        )


def get_current_date() -> str:
    """
    Returns current date
    """
    date = datetime.date.today()
    return str(date)


def get_current_time() -> str:
    """
    Returns current time (accurate to the second)
    """
    time = datetime.datetime.now().time()
    return str(time)[:8]


def meal_from_dict(meal_data: dict) -> Meal:
    """
    Returns meal object created from meal database data
    """
    meal = Meal(
        user_id=meal_data["user_id"],
        meal_id=meal_data["meal_id"],
        dish=meal_data["meal_name"],
        meal_size=meal_data["meal_size"],
        average_calories=meal_data["meal_average_calories"],
        average_proteins=meal_data["meal_average_proteins"],
        average_fats=meal_data["meal_average_fats"],
        average_carbs=meal_data["meal_average_carbs"],
        date=meal_data["meal_date"],
        time=meal_data["meal_time"],
    )
    return meal


def calculate_calories_for_day(user_id: int) -> float:
    """
    Returns the number of calories consumed by the user for 1 day
    """
    raw_info = umd.get_user_meal_for_day(user_id)
    calories_for_day = 0
    for i in range(len(raw_info)):
        calories_for_day += (
            raw_info[i]["meal_average_calories"] * raw_info[i]["meal_mass"] / 100
        )
    return calories_for_day


def calculate_proteins_for_day(user_id: int) -> float:
    """
    Returns the number of proteins consumed by the user in 1 day
    """
    raw_info = umd.get_user_meal_for_day(user_id)
    proteins_for_day = 0
    for i in range(len(raw_info)):
        proteins_for_day += (
            raw_info[i]["meal_average_proteins"] * raw_info[i]["meal_mass"] / 100
        )
    return proteins_for_day


def calculate_fats_for_day(user_id: int) -> float:
    """
    Returns the number of fats consumed by the user in 1 day
    """
    raw_info = umd.get_user_meal_for_day(user_id)
    fats_for_day = 0
    for i in range(len(raw_info)):
        fats_for_day += (
            raw_info[i]["meal_average_fats"] * raw_info[i]["meal_mass"] / 100
        )
    return fats_for_day


def calculate_carbs_for_day(user_id: int) -> float:
    """
    Returns the number of carbs consumed by the user in 1 day
    """
    raw_info = umd.get_user_meal_for_day(user_id)
    carbs_for_day = 0
    for i in range(len(raw_info)):
        carbs_for_day += (
            raw_info[i]["meal_average_carbs"] * raw_info[i]["meal_mass"] / 100
        )
    return carbs_for_day


def calculate_calories_for_week(user_id: int) -> float:
    """
    Returns the number of calories consumed by the user for 7 days
    """
    raw_info = umd.get_user_meal_for_week(user_id)
    calories_for_week = 0
    for i in range(len(raw_info)):
        calories_for_week += (
            raw_info[i]["meal_average_calories"] * raw_info[i]["meal_mass"] / 100
        )
    return calories_for_week


def calculate_proteins_for_week(user_id: int) -> float:
    """
    Returns the number of proteins consumed by the user in 7 days
    """
    raw_info = umd.get_user_meal_for_week(user_id)
    proteins_for_week = 0
    for i in range(len(raw_info)):
        proteins_for_week += (
            raw_info[i]["meal_average_proteins"] * raw_info[i]["meal_mass"] / 100
        )
    return proteins_for_week


def calculate_fats_for_week(user_id: int) -> float:
    """
    Returns the number of fats consumed by the user in 7 days
    """
    raw_info = umd.get_user_meal_for_week(user_id)
    fats_for_week = 0
    for i in range(len(raw_info)):
        fats_for_week += (
            raw_info[i]["meal_average_fats"] * raw_info[i]["meal_mass"] / 100
        )
    return fats_for_week


def calculate_carbs_for_week(user_id: int) -> float:
    """
    Returns the number of carbs consumed by the user in 7 days
    """
    raw_info = umd.get_user_meal_for_week(user_id)
    carbs_for_week = 0
    for i in range(len(raw_info)):
        carbs_for_week += (
            raw_info[i]["meal_average_carbs"] * raw_info[i]["meal_mass"] / 100
        )
    return carbs_for_week


def calculate_calories_for_month(user_id: int) -> float:
    """
    Returns the number of calories consumed by the user for 31 days
    """
    raw_info = umd.get_user_meal_for_month(user_id)
    calories_for_month = 0
    for i in range(len(raw_info)):
        calories_for_month += (
            raw_info[i]["meal_average_calories"] * raw_info[i]["meal_mass"] / 100
        )
    return calories_for_month


def calculate_proteins_for_month(user_id: int) -> float:
    """
    Returns the number of proteins consumed by the user in 31 days
    """
    raw_info = umd.get_user_meal_for_month(user_id)
    proteins_for_month = 0
    for i in range(len(raw_info)):
        proteins_for_month += (
            raw_info[i]["meal_average_proteins"] * raw_info[i]["meal_mass"] / 100
        )
    return proteins_for_month


def calculate_fats_for_month(user_id: int) -> float:
    """
    Returns the number of fats consumed by the user in 31 days
    """
    raw_info = umd.get_user_meal_for_month(user_id)
    fats_for_month = 0
    for i in range(len(raw_info)):
        fats_for_month += (
            raw_info[i]["meal_average_fats"] * raw_info[i]["meal_mass"] / 100
        )
    return fats_for_month


def calculate_carbs_for_month(user_id: int) -> float:
    """
    Returns the number of carbs consumed by the user in 31 days
    """
    raw_info = umd.get_user_meal_for_month(user_id)
    carbs_for_month = 0
    for i in range(len(raw_info)):
        carbs_for_month += (
            raw_info[i]["meal_average_carbs"] * raw_info[i]["meal_mass"] / 100
        )
    return carbs_for_month


if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
    # print(calculate_calories_for_week(1983880200))
    # print(calculate_calories_for_month(1983880200))
    print(datetime.time(10, 50, 0, 0))
