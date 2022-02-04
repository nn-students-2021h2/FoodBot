from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters,
)
from handlers import *


def main():
    bot = Updater(
        token="5038288042:AAHIZfCj2HqCmUlTrVMt5oQU5TmHAL9Fcco", use_context=True
    )
    dispatcher = bot.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex("Познакомиться"), acquaintance)],
            states={
                "user_name": [MessageHandler(Filters.text, get_user_name)],
                "user_birth_date": [MessageHandler(Filters.text, get_user_birth_date)],
                "user_sex": [
                    MessageHandler(Filters.regex("Мужской|Женский"), get_user_sex)
                ],
                "user_height": [MessageHandler(Filters.text, get_user_height)],
                "user_weight": [MessageHandler(Filters.text, get_user_weight)],
                "user_activity": [
                    MessageHandler(
                        Filters.regex("Нулевая|Слабая|Средняя|Высокая|Экстремальная"),
                        get_user_activity,
                    )
                ],
                "user_goal": [
                    MessageHandler(
                        Filters.regex("Похудение|Поддержание формы|Набор массы"),
                        get_user_goal,
                    )
                ],
            },
            fallbacks=[],
        )
    )
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex("У меня уже есть дневник"), existing_user)
            ],
            states={
                "update_data": [
                    MessageHandler(
                        Filters.regex("Изменить персональные данные"), update_data
                    )
                ],
            },
            fallbacks=[],
        )
    )

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
