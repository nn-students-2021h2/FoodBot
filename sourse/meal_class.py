class Meal:
    def __init__(
        self,
        user_id: int,
        meal_id: int,
        dish: str,
        meal_size: int,
        average_calories: int = 0,
        average_proteins: int = 0,
        average_fats: int = 0,
        average_carbohydrates: int = 0,
        date: str = None,
        time: str = None,
    ):
        self.user_id = user_id
        self.meal_id = meal_id
        self.dish = dish
        self.meal_size = meal_size
        self._calories = (average_calories/100)*meal_size
        self._proteins = (average_proteins/100)*meal_size
        self._fats = (average_fats/100)*meal_size
        self._carbohydrates = (average_carbohydrates/100)*meal_size
        self.date = date
        self.time = time

    def count_nutrients(self):
        """
        counts nutrition facts based on dish data stored in dish_database
        """
        pass

    def meal_to_database(self):
        """
        Adds each dish to a database
        """
        pass
