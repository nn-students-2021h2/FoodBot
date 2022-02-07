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
                MessageHandler(Filters.regex("Go"), existing_user),
                MessageHandler(Filters.regex("Начнем"), existing_user),
            ],
            states={
                "origin_state": [MessageHandler(Filters.text, existing_user)],
                "update_existing_user_data": [
                    MessageHandler(
                        Filters.regex("Изменить персональные данные"),
                        update_existing_user_data,
                    )
                ],
                "update_existing_user_data_continue": [MessageHandler(Filters.text, update_existing_user_data_continue)],
                "update_exiting_user_name": [MessageHandler(Filters.text, update_exiting_user_name)],
                "update_exiting_user_age": [MessageHandler(Filters.text, update_exiting_user_age)],
                "update_exiting_user_sex": [MessageHandler(Filters.text, update_exiting_user_sex)],
                "update_exiting_user_height": [MessageHandler(Filters.text, update_exiting_user_height)],
                "update_exiting_user_weight": [MessageHandler(Filters.text, update_exiting_user_weight)],
                "update_exiting_user_activity": [MessageHandler(Filters.text, update_exiting_user_activity)],
                "update_exiting_user_goal": [MessageHandler(Filters.text, update_exiting_user_goal)],
                "update_exiting_user_norm": [MessageHandler(Filters.text, update_exiting_user_norm)]
            },
            fallbacks=[],
        )
    )

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
