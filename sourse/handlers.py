from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from utils import initial_keyboard, existing_user_keyboard
from time import sleep
from user_class import User
from user_database import delete_note_with_id, get_user_object
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    print("Кто-то запустил бота!")
    print("Удаляю имеющуюся запись")
    delete_note_with_id(update.effective_chat.id)
    update.message.reply_text(
        f"{update.message.chat.first_name}, Вас приветствует Foodbot. "
        f"Прежде чем начать работу, мне нужно узнать кое-что о вас. "
        f"Давайте познакомимся!",
        reply_markup=initial_keyboard(),
    )


def acquaintance(update: Update, context: CallbackContext) -> str:
    update.message.reply_text(
        "Как к Вам обращаться? Введите имя или псевдоним: ",
        reply_markup=ReplyKeyboardRemove(),
    )
    return "user_name"


def get_user_name(update: Update, context: CallbackContext) -> str:
    context.user_data["name"] = update.message.text
    update.message.reply_text(f"{update.message.text.capitalize()}, cколько Вам лет? ")
    return "user_birth_date"


def get_user_birth_date(update: Update, context: CallbackContext) -> str:
    context.user_data["birth_date"] = update.message.text
    reply_keyboard = [["Мужской", "Женский"]]
    update.message.reply_text(
        "Укажите свой пол:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_sex"


def get_user_sex(update: Update, context: CallbackContext) -> str:
    context.user_data["sex"] = update.message.text
    update.message.reply_text("Введите ваш рост в сантиметрах (например, 180): ")
    return "user_height"


def get_user_height(update: Update, context: CallbackContext) -> str:
    context.user_data["height"] = update.message.text
    update.message.reply_text("Введите ваш вес в килограммах (например, 74): ")
    return "user_weight"


def get_user_weight(update: Update, context: CallbackContext) -> str:
    context.user_data["weight"] = update.message.text
    reply_keyboard = [["Нулевая", "Слабая", "Средняя", "Высокая", "Экстремальная"]]
    update.message.reply_text(
        "Какой у Вас уровень активности? <добавить пояснения>",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_activity"


def get_user_activity(update: Update, context: CallbackContext) -> str:
    context.user_data["activity"] = update.message.text
    reply_keyboard = [["Похудение", "Поддержание формы", "Набор массы"]]
    update.message.reply_text(
        "Какая у вас цель? <добавить пояснения>",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "user_goal"


def get_user_goal(update: Update, context: CallbackContext) -> None:
    context.user_data["goal"] = update.message.text
    update.message.reply_text(
        f'Отлично, {context.user_data["name"].capitalize()}! '
        f"Теперь я могу подсчитать вашу норму калорий и нутриентов. "
        f"Дайте мне секунду..."
    )
    sleep(1)
    user = User(
        user_id=update.message.chat.id,
        name=context.user_data["name"],
        age=context.user_data["birth_date"],
        sex=context.user_data["sex"],
        height=context.user_data["height"],
        weight=context.user_data["weight"],
        activity=context.user_data["activity"],
        goal=context.user_data["goal"],
    )
    update.message.reply_text(user.get_short_info())
    user.user_to_database()


def existing_user(update: Update, context: CallbackContext) -> str:
    user_name = get_user_object(user_id=update.message.chat.id)["user_name"]
    update.message.reply_text(
        f"{user_name}, я рад тебя видеть! Чем я могу тебе помочь?",
        reply_markup=existing_user_keyboard(),
    )
    return "update_existing_user_data"


def update_existing_user_data(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [["Имя", "Возраст", "Пол"], ["Уровень активности", "Цель"]]
    update.message.reply_text(
        "Какую информацию ты хочешь изменить?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
