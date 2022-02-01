import logging
from user_database import *
from human_class import User
from meal_class import Meal
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Здравстуйте, {update.effective_user.first_name}!"
        f" Вас приветствует FoodBot!\n"
        f" Давайте вычислим вашу норму калорийности",
    )
    acquaintance(update, context)


def hello(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Зарегистрировать прием пищи", callback_data="add_meal")],
        [
            InlineKeyboardButton(
                "Вспомнить свою норму КБЖУ", callback_data="nutrients_norm"
            )
        ],
        [InlineKeyboardButton("Посмотреть статистику", callback_data="statistics")],
        [
            InlineKeyboardButton(
                "Обновить персональные данные", callback_data="update_user_data"
            )
        ],
        [
            InlineKeyboardButton(
                "Сбросить и переопределить все данные", callback_data="acquaintance"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "И снова здравствуй! Чем займемся?", reply_markup=reply_markup
    )


def buttons(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    query.answer()
    choice = query.data

    user = get_current_user()

    if choice == "acquaintance":
        delete_note_with_id(update.effective_chat.id)
        acquaintance(update, context)
    elif choice == "update_user_data":
        update_user_data(update, context, user)
    elif choice == "nutrients_norm":
        nutrients_norm(update, context, user)
    elif choice == "add_meal":
        add_meal(update, context, user)
    elif choice == "statistics":
        statistics(update, context, user)


def acquaintance(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Сколько вам лет? "))
    user_sex = input("Укажите ваш пол(мужской, женский): ")
    user_height = int(input("Какой у вас рост? Введите число в сантиметрах: "))
    user_weight = int(input("Какой у вас вес? Введите число в килограммах: "))
    user_activity = input(
        "Укажите ваш уровень активности (нулевая, слабая, средняя, высокая, экстремальная): "
    )
    user_goal = input("Укажите вашу цель (поддержание формы, похудение, набор массы): ")

    user = User(
        user_id,
        user_name,
        user_age,
        user_sex,
        user_height,
        user_weight,
        user_activity,
        user_goal,
    )
    # print(user_id)
    # user = User(user_id, "Иван", 30, "мужской", 180, 120, "слабая", "похудение")
    user.user_to_database()


def update_user_data(update: Update, context: CallbackContext, user: User) -> None:
    print("update_user_data")


def nutrients_norm(update: Update, context: CallbackContext, user: User):
    print("nutrients_norm")


def add_meal(update: Update, context: CallbackContext, user: User):
    print("add_meal")


def statistics(update: Update, context: CallbackContext, user: User):
    print("statistics")


# This handler MUST be added last. If you added it sooner,
# it would be triggered before the CommandHandlers had a chance to look at the update
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что-что? Я не понял :( "
    )


# additional functions


def get_current_user() -> User:
    """
    return user object
    """


def take_user_meal() -> Meal:
    """
    return meal object
    """


def main():
    updater = Updater(
        token="5038288042:AAHIZfCj2HqCmUlTrVMt5oQU5TmHAL9Fcco", use_context=True
    )
    dispatcher = updater.dispatcher

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    # bot = Bot(
    #     token=TOKEN,
    #     base_url=PROXY,  # delete it if connection via VPN
    # )
    # updater = Updater(bot=bot, use_context=True)

    # Connect via socks proxy
    REQUEST_KWARGS = {
        #'proxy_url': PROXY,  # Uncomment this line if you encounter network issues/timeouts when starting the bot
        # Fill in the PROXY variable in setup.py with a proper proxy URL for this to work.
        # Optional, if you need authentication:
        # 'urllib3_proxy_kwargs': {
        #     'username': 'name',
        #     'password': 'passwd',
        # }
    }

    # call function every time the Bot receives a Telegram message that contains the corresponding command
    start_handler = CommandHandler("start", start)
    hello_handler = CommandHandler("hello", hello)
    # meal_handler = CommandHandler('meal', add_meal)
    # meal_button_handler = CallbackQueryHandler(add_meal)
    unknown_handler = MessageHandler(Filters.command, unknown)

    # as soon as you add new handlers to dispatcher, they are in effect
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)
    # dispatcher.add_handler(meal_handler)
    # dispatcher.add_handler(meal_button_handler)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(CallbackQueryHandler(buttons))

    # launch the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
