#import logging

#from telegram import Bot, Update
#from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater


class User:

    def __init__(self, name, age, sex, height, weight, activity, goal):
        """Constructor"""
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity = activity
        self.goal = goal
        self.calorie_norm = 0
        self.protein_norm = 0
        self.fat_norm = 0
        self.carbohydrate_norm = 0

    def count_norm(self):
        """
        Counts daily norm of nutrients according to user's attributes
        Source: https://edatop.ru/252-raschet-bzhu.html#hmenu-10
        """

        activity_cf = {
            'нулевая': 1.2,
            'слабая': 1.375,
            'средняя': 1.55,
            'высокая': 1.7,
            'экстремальная': 1.9
        }

        # (proteins, fats, carbs) aka (б, ж, у)
        goal_cf = {
            'поддержание формы': (0.3, 0.3, 0.4),
            'похудение': (0.25, 0.25, 0.5),
            'набор массы': (0.35, 0.3, 0.55)
        }

        if self.sex == 'женский':
            self.calorie_norm = round(447.6 + 9.2 * self.weight + 3.1 * self.height - 4.3 * self.age)
        elif self.sex == 'мужской':
            self.calorie_norm = round(88.36 + 13.4 * self.weight + 4.8 * self.height - 5.7 * self.age)
        self.calorie_norm *= activity_cf[self.activity]

        PROTEIN_IN_KCAL, CARB_IN_KCAL, FAT_IN_KCAL = 4, 4, 9
        
        self.protein_norm = round(self.calorie_norm * goal_cf[self.goal][0] / PROTEIN_IN_KCAL)
        self.fat_norm = round(self.calorie_norm * goal_cf[self.goal][1] / FAT_IN_KCAL)
        self.carbohydrate_norm = round(self.calorie_norm * goal_cf[self.goal][2] / CARB_IN_KCAL)
        
        return f'{self.name.title()}, ваша дневная норма калорий — {self.calorie_norm} ккал. \n' \
               f'Белки: {self.protein_norm} г. \n' \
               f'Жиры: {self.fat_norm} г. \n' \
               f'Углеводы: {self.carbohydrate_norm} г.'

    def user_to_database(self):
        """
        adds user data to user_database
        """
        pass
