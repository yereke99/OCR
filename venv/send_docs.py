from aiogram.dispatcher.filters.state import StatesGroup, State
from logger import  bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from data_base import cursor, db
import datetime, telegram_bot

zayavka_path = r'C:\Users\Yerek\PycharmProjects\new_system\zayavka'
file_path = r'C:\Users\Yerek\PycharmProjects\new_system\venv\docs'

class Receive_docs(StatesGroup):
    q1 = State()
    #q2 = State()

@dp.message_handler(Command('send'), state=None)
async def start_send_doc(message: types.Message):
    await message.answer("Компания қызметкерлерінің👥 id-ын енгізіңіз")
    await Receive_docs.q1.set()

@dp.message_handler(state=Receive_docs.q1)
async def qu1(message: types.Message, state=FSMContext):
    answer = int(message.text)
    if answer == 123147159:
        await message.answer("Құжатты жіберу үшін /senddoc басыңыз")
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, "Енгізген ID қате❌\nҚайтадан /tap түймесін басып жазыңыз!")
        await state.finish()


'''@dp.message_handler(state=Receive_docs.q2)
async def receive(message: types.Message, state=FSMContext):


    await Receive_docs.finish()
'''