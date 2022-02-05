class Meal:
    def __init__(
        self,
        dish: str,
        portion_size: int,
        measure_units: str,
        date: str = None,
        time: str = None,
    ):
        self.dish = dish
        self.portion_size = portion_size
        self.measure_units = measure_units
        self.date = date
        self.time = time
        self._calories = 0
        self._proteins = 0
        self._fats = 0
        self._carbohydrates = 0

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
