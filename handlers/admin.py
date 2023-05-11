from aiogram import types



async def example(message: types.Message):
    chat_type = message.chat.type
    reply = message.reply_to_message
    member_type = await message.chat.get_member(
        message.from_user.id
    )
    member_type = member_type['status']
    await message.answer(f"{chat_type=}, {reply=}, {member_type=}")
    if message.chat.type != 'private':
        # group
        pass
    if message.reply_to_message:
        pass
    if member_type != 'member':
        # 'admin'
        # 'creator
        pass


async def check_bad_words(message: types.Message):
    bad_words = ('дурак', 'дурень')
    if message.chat.type != 'private':
        text = message.text
        for word in bad_words:
            if word in text.lower().replace(' ', ''):
                await message.reply('Нельзя так выражаться')
                break


async def pin_message(message: types.Message):
    if message.chat.type != 'private' and message.reply_to_message:
        await message.reply_to_message.pin()


async def check_admin_group_and_reply(message: types.Message):
    member_type = await message.chat.get_member(
        message.from_user.id
    )
    return message.chat.type != 'private' and message.reply_to_message and member_type['status'] != 'member'


async def ban_user(message: types.Message):
    check = await check_admin_group_and_reply(message)
    if check:
        author = message.reply_to_message.from_user.id
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=author
        )
