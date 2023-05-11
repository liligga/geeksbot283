from aiogram import types
from config import scheduler, bot
from datetime import datetime


async def start_reminder(message: types.Message):
    # для интервала
    # scheduler.add_job(
    #     send_reminder, 
    #     'interval', 
    #     seconds=5, 
    #     args=(message.from_user.id,)
    # )
    # для конкретной одной даты
    # scheduler.add_job(
    #     send_reminder,
    #     'date',
    #     run_date=datetime(year=2023, month=5, day=1, hour=17, minute=45),
    #     args=(message.from_user.id, message.text)
    # )
    # для крона
    # year: int|str 4 цифры  2023|"2023"
    # month: int|str 1-12
    # day: int|str число месяца 1-31
    # week: int|str число недели в году 1-53
    # day_of_week: int|str 0-6, "mon", "tue", ... "sun"
    # hour: int|str 0-23
    # minute: int|str 0-59
    # second: int|str 0-59
    scheduler.add_job(
        # print(dir(send_reminder))
        send_reminder,
        'cron',
        # month=5, day_of_week="mon-fri", hour=16, minute="49,50",
        day_of_week="sat", hour=17, minute=11,
        # week="1-10". day_of_week="mon"
        args=(message.from_user.id,)
    )
    await message.answer("Слушаю и повинуюсь!")


async def send_reminder(user_id: int, text: str = "Напомни"):
    await bot.send_message(
        chat_id=user_id,
        text=text
    )
