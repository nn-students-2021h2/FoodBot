#import logging

#from telegram import Bot, Update
#from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater


class User:

    def __init__(self, name, height, weight, age, sex):
        """Constructor"""
        # аргументы, к-е получаем от юзера, кладем в инит в виде аргументов
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        # данные, которые будем высчитывать самостоятельно, по умолчанию зануляем
        self.calorie_norm = 0
        self.protein_norm = 0
        self.fat_norm = 0
        self.carbohydrate_norm = 0

    # здесь можете наблюдать использование инит-атрибутов в методе класса
    def count_norm(self):
        """Counts daily norm of nutrients based on user's attributes
        Source: https://stolichki.ru/stati/kak-opredelit-sutochnuyu-normu-kaloriy"""
        if self.sex == 'female':
            self.calorie_norm = 447.6 + 9.2 * self.weight + 3.1 * self.height - 4.3 * self.age
        elif self.sex == 'male':
            self.calorie_norm = 88.36 + 13.4 * self.weight + 4.8 * self.height - 5.7 * self.age
        return f'Your daily norm of calories is {self.calorie_norm}'

    def add_to_database(self):
        pass



    def meal(self):
        """
        Registers each dish
        """
        pass

# ботоподобные запросы, запускайте код и вбивайте какой-нибудь текст (я пока не знаю как это реализовать с помощью тг)
username = input('Please enter your name: ')
user_height = int(input('Please enter your height: '))
user_weight = int(input('Please enter your weight: '))
user_age = int(input('Please enter your age: '))
user_sex = input('Please enter your sex: ')

# создаем объект юзера только после того, как получили от него нужные параметры
user = User(username, user_height, user_weight, user_age, user_sex)

# ВАЖНО!!! МЕТОДЫ вызываем СО СКОБКАМИ, АТРИБУТЫ получаем БЕЗ СКОБОК
print(user.count_norm())
print(f"{user.name}'s norm of calories is {user.calorie_norm}!")
