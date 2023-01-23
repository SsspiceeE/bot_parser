from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import start
from utils.parse_prices import parse_prices

from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=start.main)


@dp.message_handler(text_contains='Получить цены 🧾')
async def get_prices(message: types.Message):
    message_to_delete = await message.answer('Пожалуйста, подождите 🕗')
    parse_prices()
    file = InputFile(path_or_bytesio='shtukaturka.csv')
    await message.answer_document(document=file)
    await dp.bot.delete_message(chat_id=message.from_user.id, message_id=message_to_delete.message_id)





