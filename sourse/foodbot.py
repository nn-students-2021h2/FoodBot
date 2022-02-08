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
                "main_state": [
                    MessageHandler(Filters.regex("Продолжить"), existing_user),
                    MessageHandler(
                        Filters.regex("Вспомнить свою норму КБЖУ"), get_cpfc_norm
                    ),
                    MessageHandler(
                        Filters.regex("Изменить персональные данные"),
                        update_existing_user_data,
                    ),
                ],
                "update_existing_user_data": [
                    MessageHandler(Filters.regex("Имя"), pre_update_exiting_user_name),
                    MessageHandler(
                        Filters.regex("Возраст"), pre_update_exiting_user_age
                    ),
                    MessageHandler(Filters.regex("Пол"), pre_update_exiting_user_sex),
                    MessageHandler(
                        Filters.regex("Рост"), pre_update_exiting_user_height
                    ),
                    MessageHandler(
                        Filters.regex("Вес"), pre_update_exiting_user_weight
                    ),
                    MessageHandler(
                        Filters.regex("Уровень активности"),
                        pre_update_exiting_user_activity,
                    ),
                    MessageHandler(Filters.regex("Цель"), pre_update_exiting_user_goal),
                    MessageHandler(
                        Filters.regex("Вернуться в основное меню"), return_to_main_state
                    ),
                ],
                "update_exiting_user_name": [
                    MessageHandler(Filters.text, update_exiting_user_name)
                ],
                "update_exiting_user_age": [
                    MessageHandler(Filters.text, update_exiting_user_age)
                ],
                "update_exiting_user_sex": [
                    MessageHandler(Filters.text, update_exiting_user_sex)
                ],
                "update_exiting_user_height": [
                    MessageHandler(Filters.text, update_exiting_user_height)
                ],
                "update_exiting_user_weight": [
                    MessageHandler(Filters.text, update_exiting_user_weight)
                ],
                "update_exiting_user_activity": [
                    MessageHandler(Filters.text, update_exiting_user_activity)
                ],
                "update_exiting_user_goal": [
                    MessageHandler(Filters.text, update_exiting_user_goal)
                ],
                "update_exiting_user_norm": [
                    MessageHandler(Filters.text, update_exiting_user_norm)
                ],
            },
            fallbacks=[],
        )
    )

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
