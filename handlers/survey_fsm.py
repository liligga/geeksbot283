from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


# Finite State Machine
class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()


async def start_survey(message: types.Message):
    await Survey.name.set()

    await message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Survey.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Введите цифры")
    elif int(age) > 100 or int(age) < 10:
        await message.answer("Введите нормальный возраст")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
            print(data)

        # await Survey.next()
        # await message.answer("Ваш пол?")
        await state.finish()












