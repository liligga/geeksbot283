from aiogram import types
from db.base import get_products


async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("Всё"))
    kb.add(types.KeyboardButton("Книги"), types.KeyboardButton("Сувениры"))
    await message.answer(
        f"Выберите категорию ниже:",
        reply_markup=kb
    )
    


async def show_books(message: types.Message):

    await message.reply(
        "Вот наши книги",
        reply_markup=types.ReplyKeyboardRemove()
    )
    for pr in get_products():
        # print(pr)
        # (1, 'Самая лучшая книга', 200, 'images/cat.webp')
        # (2, 'Самая интересная книга', 400, 'images/cat.webp')
        with open(pr[3], 'rb') as product_pic:
            await message.answer_photo(
                product_pic, 
                caption=f"Товар: {pr[1]} по цене {pr[2]}")