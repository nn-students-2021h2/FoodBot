from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from utils import keyboards
from time import sleep
from user_class import User


def start(bot, update):
    print("Кто-то запустил бота!")
    bot.message.reply_text(
        f"{bot.message.chat.first_name}, Вас приветствует Foodbot. "
        f"Прежде чем начать работу, мне нужно узнать кое-что о вас. "
        f"Давайте познакомимся!",
        reply_markup=keyboards(),
    )


def acquaintance(bot, update):
    bot.message.reply_text(
        "Как к Вам обращаться? Введите имя или псевдоним: ",
        reply_markup=ReplyKeyboardRemove(),
    )
    return "user_name"


def get_user_name(bot, update):
    update.user_data["name"] = bot.message.text
    bot.message.reply_text(f"{bot.message.text.capitalize()}, cколько Вам лет? ")
    return "user_birth_date"


def get_user_birth_date(bot, update):
    update.user_data["birth_date"] = bot.message.text
    reply_keyboard = [["Мужской", "Женский"]]
    bot.message.reply_text(
        "Укажите свой пол:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_sex"


def get_user_sex(bot, update):
    update.user_data["sex"] = bot.message.text
    bot.message.reply_text("Введите ваш рост в сантиметрах (например, 180): ")
    return "user_height"


def get_user_height(bot, update):
    update.user_data["height"] = bot.message.text
    bot.message.reply_text("Введите ваш вес в килограммах (например, 74): ")
    return "user_weight"


def get_user_weight(bot, update):
    update.user_data["weight"] = bot.message.text
    reply_keyboard = [["Нулевая", "Слабая", "Средняя", "Высокая", "Экстремальная"]]
    bot.message.reply_text(
        "Какой у Вас уровень активности? <добавить пояснения>",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_activity"


def get_user_activity(bot, update):
    update.user_data["activity"] = bot.message.text
    reply_keyboard = [["Похудение", "Поддержание формы", "Набор массы"]]
    bot.message.reply_text(
        "Какая у вас цель? <добавить пояснения>",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_goal"


def get_user_goal(bot, update):
    update.user_data["goal"] = bot.message.text
    bot.message.reply_text(
        f'Отлично, {update.user_data["name"].capitalize()}! '
        f"Теперь я могу подсчитать вашу норму калорий и нутриентов. "
        f"Дайте мне секунду..."
    )
    sleep(1)
    user = User(
        user_id=bot.message.chat.id,
        name=update.user_data["name"],
        age=update.user_data["birth_date"],
        sex=update.user_data["sex"],
        height=update.user_data["height"],
        weight=update.user_data["weight"],
        activity=update.user_data["activity"],
        goal=update.user_data["goal"],
    )
    bot.message.reply_text(user.count_norm())
    user.to_database()


def existing_user(bot, update):
    user_name = get_user_object(user_id=bot.message.chat.id)["user_name"]
    bot.message.reply_text(
        f"{user_name}, я рад тебя видеть! Чем я могу тебе помочь?",
        reply_markup=existing_user_keyboard(),
    )
    return "user_data"
