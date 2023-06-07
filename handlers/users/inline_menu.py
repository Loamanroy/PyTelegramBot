from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_test
from keyboards.inline import ikb_menu
from loader import dp


@dp.message_handler(text='Inline menu')
async def show_inline_menu(message: types.Message):
    await message.answer("Inline button are below", reply_markup=ikb_menu)


@dp.callback_query_handler(text="Message")
async def send_message(call: CallbackQuery):
    await call.message.answer("Buttons are changed", reply_markup=kb_test)


@dp.callback_query_handler(text="Alert")
async def send_message(call: CallbackQuery):
    await call.answer("Buttons are changed")
