from loader import dp

from aiogram import types
from utils.db_api.quickcommands import register_user


@dp.message_handler(commands=['register'])
async def command_start(message: types.Message):
    user = register_user(message)
    if user:
        await message.answer('Вы успешно зарегистрировались!')
    else:
        await message.answer('Вы уже зарегистрированы!')
