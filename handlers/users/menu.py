from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import kb_menu

from loader import dp


@dp.message_handler(Command("Menu"))
async def menu(message: types.Message):
    await message.answer(text="Some text", reply_markup=kb_menu)
