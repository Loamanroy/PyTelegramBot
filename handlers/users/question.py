from aiogram import types
from loader import dp

from filters import IsPrivate


@dp.message_handler(IsPrivate(), text='/question')
async def command_question(message: types.Message):
    await message.answer(f"Привет,{message.from_user.full_name}, Какой у тебя вопрос? \n")
