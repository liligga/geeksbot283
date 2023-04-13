from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, italic, bold, spoiler
from dotenv import load_dotenv
import os
from handlers.info import info, echo


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "go"])
async def start(message: types.Message):
    # print(dir(message.from_user))
    first_name = message.from_user.first_name
    id = message.from_user.id
    await message.answer(f"Приветствуем тебя, пользователь {first_name}, {id}")
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text="Приветствуем тебя, пользователь"
    # )


@dp.message_handler(commands=["pic"])
async def picture(message: types.Message):
    with open('images/cat.webp', 'rb') as photo:
        await message.reply_photo(
            photo,
            caption="Умный кот 😂😼"
        )


@dp.message_handler(commands=["sticker"])
async def sticker(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEIhVxkMuljwGZFnSoou7p4LED1AAHHjWgAAtguAAK1LqFLRUS7pDThxU8vBA")
    await message.answer("Sticker cat")




if __name__ == "__main__":
    dp.register_message_handler(info, commands=["info"])

    # этот обработчик обрабатывает все сообщения поэтому он ниже всех
    dp.register_message_handler(echo)

    executor.start_polling(dp)
