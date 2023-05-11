from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp, scheduler
from handlers.admin import ban_user, check_bad_words, example, pin_message
from handlers.info import info, echo
from handlers.start import start, about
from handlers.shop import show_categories, show_books
from handlers.survey_fsm import (
    start_survey,
    process_name,
    process_age,
    process_gender,
    Survey    
)
from db.base import (
    init_db,
    create_tables,
    insert_products,
    delete_products
)
from scheduler.reminder import start_reminder
import logging


async def start_up(_):
    init_db()
    delete_products()
    create_tables()
    insert_products()
    # read_bad_words_list()




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # обработчики
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(example, commands=["example"])
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(ban_user, commands=["ban"], commands_prefix='!')
    dp.register_callback_query_handler(about, lambda cb: cb.data == "about")
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_books, Text(equals="Книги"))
    dp.register_message_handler(show_books, Text(startswith="напомни"))
    # dp.register_message_handler(show_books, Text(contains="Книги"))
    # dp.register_message_handler(show_books, Text(startswith="Книги"))

    # Опросник FSM
    dp.register_message_handler(start_survey, commands=["surv"])
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(process_gender, state=Survey.gender)

    # Напоминалка
    dp.register_message_handler(start_reminder, commands=["rem"])

    # этот обработчик обрабатывает все сообщения поэтому он ниже всех
    dp.register_message_handler(check_bad_words)

    scheduler.start()
    executor.start_polling(dp, on_startup=start_up)
