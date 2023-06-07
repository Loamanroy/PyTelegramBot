from aiogram import types
from loader import dp

from filters import IsPrivate
from utils.misc.throttling import rate_limit


@rate_limit(limit=5, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f"Привет,{message.from_user.full_name} \n"
                         f"Твой ID = {message.from_user.id}")
