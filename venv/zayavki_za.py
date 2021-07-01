from aiogram.dispatcher.filters.state import StatesGroup, State
from logger import  bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from data_base import cursor, db
import datetime


zayavka_path = r'C:\Users\Yerek\PycharmProjects\new_system\zayavka'

class Test(StatesGroup):
    Q1 = State() # name of client
    Q2 = State() # surname of client
    Q3 = State() # whats up?
    Q4 = State() # telephone number

@dp.message_handler(Command('zayavki'), state=None)
async def start_order_kz(message: types.Message):
    await message.answer("Есіміңіз")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def qu1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Тегіңіз")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def qu2(message: types.Message, state=FSMContext):
    answer = message.text
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Өтінішіңізді қысқаша жазып кетсеңіз✍🏻")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def qu3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Телефон номеріңіз📱?")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def qu4(message: types.Message, state=FSMContext):
    answer = int(message.text)
    global ans4
    ans4 = answer
    await state.update_data(answer4 = answer)
    d_t = datetime.datetime.today()
    data_t = str(d_t)
    data = await state.get_data()
    cursor.execute("INSERT INTO client_za(n, s, tele, data, type, c) VALUES(%s, %s, %s, %s, %s, %s)",
                   (ans1, ans2, ans3, data_t, ans4, "false",))
    db.commit()

    await bot.send_message(message.from_user.id, "Жазған✍🏻 өтінішіңіз қабылданды жақын арада сізге хабарласамыз📞")
    await state.finish()


