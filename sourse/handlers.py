from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from utils import initial_keyboard, existing_user_keyboard
from time import sleep
from user_class import User, user_from_dict
from user_database import *
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
    user.count_norm()
    update.message.reply_text(user.get_short_info())
    user.user_to_database()


def existing_user(update: Update, context: CallbackContext) -> str:
    user_name = get_user_object(user_id=update.message.chat.id)["user_name"]
    update.message.reply_text(
        f"{user_name}, я рад тебя видеть! Чем я могу тебе помочь?",
        reply_markup=existing_user_keyboard(),
    )
    return "update_existing_user_data"


def update_existing_user_data(update: Update, context: CallbackContext) -> str:
    reply_keyboard = [
        ["Имя", "Возраст", "Пол"],
        ["Вес", "Рост"],
        ["Уровень активности", "Цель", "Вернуться в основное меню"],
    ]
    update.message.reply_text(
        "Какую информацию ты хочешь изменить?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_existing_user_data_continue"


def update_existing_user_data_continue(update: Update, context: CallbackContext) -> str:
    user_choice = update.message.text
    if user_choice == "Имя":
        update.message.reply_text("Укажите новое имя")
        return "update_exiting_user_name"
    elif user_choice == "Возраст":
        update.message.reply_text("Укажите новый возраст")
        return "update_exiting_user_age"
    elif user_choice == "Пол":
        reply_keyboard = [["Мужской", "Женский"]]
        update.message.reply_text(
            "Укажите новый пол:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return "update_exiting_user_sex"
    elif user_choice == "Рост":
        update.message.reply_text("Укажите новый рост")
        return "update_exiting_user_height"
    elif user_choice == "Вес":
        update.message.reply_text("Укажите новый вес")
        return "update_exiting_user_weight"
    elif user_choice == "Уровень активности":
        reply_keyboard = [["Нулевая", "Слабая", "Средняя", "Высокая", "Экстремальная"]]
        update.message.reply_text(
            "Укажите новый уровень активности",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return "update_exiting_user_activity"
    elif user_choice == "Цель":
        reply_keyboard = [["Похудение", "Поддержание формы", "Набор массы"]]
        update.message.reply_text(
            "Укажите новую цель",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return "update_exiting_user_goal"
    elif user_choice == "Вернуться в основное меню":
        reply_keyboard = [["Продолжить"]]
        update.message.reply_text(
            'Для продолжения взаимодестаия с ботом нажмите "Продолжить"',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return "origin_state"


def update_exiting_user_name(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_name(update.effective_chat.id, user_enter)
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_age(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_age(update.effective_chat.id, int(user_enter))
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_sex(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_sex(update.effective_chat.id, user_enter)
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_height(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_height(update.effective_chat.id, float(user_enter))
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_weight(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_weight(update.effective_chat.id, float(user_enter))
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_activity(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_activity(update.effective_chat.id, user_enter)
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_goal(update: Update, context: CallbackContext) -> str:
    user_enter = update.message.text
    update_user_goal(update.effective_chat.id, user_enter)
    reply_keyboard = [["Пересчитать норму каллорий"]]
    update.message.reply_text(
        "Изменения внесены",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "update_exiting_user_norm"


def update_exiting_user_norm(update: Update, context: CallbackContext) -> str:
    user = user_from_dict(get_user_object(update.effective_chat.id))
    user.count_norm()
    update_user_calorie_norm(update.effective_chat.id, user.calorie_norm)
    update_user_protein_norm(update.effective_chat.id, user.protein_norm)
    update_user_fat_norm(update.effective_chat.id, user.fat_norm)
    update_user_carbohydrate_norm(update.effective_chat.id, user.carbohydrate_norm)
    reply_keyboard = [["Продолжить"]]
    update.message.reply_text(
        'Для продолжения взаимодестаия с ботом нажмите "Продолжить"',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return "origin_state"
