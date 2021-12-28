import logging
from human_class import User
from meal_class import Meal
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, CommandHandler, MessageHandler, Filters

updater = Updater(token='5038288042:AAHIZfCj2HqCmUlTrVMt5oQU5TmHAL9Fcco', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    update.message.reply_text(f'Здравстуйте, {update.effective_user.first_name}! Вас приветствует FoodBot!\n'
                              f' Давайте вычислим вашу норму калорийности')


def hello(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Обновить персональные данные", callback_data='update_user_data')],
        [InlineKeyboardButton("Вспомнить свою норму КБЖУ", callback_data='nutrients_norm')],
        [InlineKeyboardButton("Зарегистрировать прием пищи", callback_data='add_meal')],
        [InlineKeyboardButton("Посмотреть статистику", callback_data='statistics')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('И снова здравствуй! Чем займемся?', reply_markup=reply_markup)


def buttons(update: Update, context: CallbackContext, user: User, meal: Meal) -> None:

    query = update.callback_query
    query.answer()
    choice = query.data

    if choice == 'acquaintance':
        update.message.reply_text('Hello! Nothing here yet')
        acquaintance(update, context)
    elif choice == 'update_user_data':
        update_user_data(update, context, user)
    elif choice == 'nutrients_norm':
        nutrients_norm(update, context, user)
    elif choice == 'add_meal':
        add_meal(update, context, user, meal)
    elif choice == 'statistics':
        statistics(update, context, user)


def acquaintance(update: Update, context: CallbackContext) -> None:
    """
    username = input('Введите ваше имя: ')
    user_age = int(input('Сколько вам лет? '))
    user_sex = input('Укажите ваш пол: ')
    user_height = int(input('Какой у вас рост? Введите число в сантиметрах: '))
    user_weight = int(input('Какой у вас вес? Введите число в килограммах: '))
    user_activity = input('Укажите ваш уровень активности (нулевая, слабая, средняя, высокая, экстремальная): ')
    user_goal = input('Укажите вашу цель (поддержание формы, похудение, набор массы: ')

    user = User(username, user_age, user_sex, user_height, user_weight, user_activity, user_goal)
    """
    # then add user to database


def update_user_data(update: Update, context: CallbackContext, user: User) -> None:
    pass


def nutrients_norm(update: Update, context: CallbackContext, user: User):
    pass


def add_meal(update: Update, context: CallbackContext, user: User, meal: Meal):
    pass


def statistics(update: Update, context: CallbackContext, user: User):
    pass


# This handler MUST be added last. If you added it sooner,
# it would be triggered before the CommandHandlers had a chance to look at the update
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Что-что? Я не понял :( ")


def main():
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
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)
    # meal_handler = CommandHandler('meal', add_meal)
    # meal_button_handler = CallbackQueryHandler(add_meal)
    unknown_handler = MessageHandler(Filters.command, unknown)

    # as soon as you add new handlers to dispatcher, they are in effect
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)
    # dispatcher.add_handler(meal_handler)
    # dispatcher.add_handler(meal_button_handler)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, hello))
    dispatcher.add_handler(CallbackQueryHandler(buttons))

    # launch the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
