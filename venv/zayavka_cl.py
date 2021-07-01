from aiogram.dispatcher.filters.state import StatesGroup, State
from logger import  bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from random import random
from aiogram.dispatcher import FSMContext
from data_base import cursor, db
import datetime

zayavka_path = r'C:\Users\Yerek\PycharmProjects\new_system\zayavka'

class test(StatesGroup):
    q1 = State()  # check id_user employee
    q2 = State()  # name of client
    q3 = State()  # surname
    q4 = State()  # telephone number
    q5 = State()  # doc file

@dp.message_handler(Command('tap'), state=None)
async def check_id(message: types.Message):
    await message.answer("Компания қызметкерлерінің👥 id-ын енгізіңіз")
    await test.q1.set()

@dp.message_handler(state=test.q1)
async def ques1(message: types.Message, state=FSMContext):
    answer = int(message.text)
    if answer == 123147159:
        await message.answer("Есіміңіз")
        await test.next()
    else:
        await bot.send_message(message.from_user.id,"Енгізген ID қате❌\nҚайтадан /tap түймесін басып жазыңыз!")
        await state.finish()


@dp.message_handler(state=test.q2)
async def ques2(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Тегіңіз")
    await test.next()

@dp.message_handler(state=test.q3)
async def ques3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Телефон номеріңіз📱?")
    await test.next()

@dp.message_handler(state=test.q4)
async def ques4(message: types.Message, state=FSMContext):
    try:
        answer = int(message.text)
        global ans3
        ans3 = answer
    except ValueError:
        await bot.send_message(message.from_user.id, "Телефон номерңізді сандармен ғана жазыңыз❗")
    await state.update_data(answer3=answer)
    await message.answer("Арыз-шағымыңыздың🗣 себебін жазаңыз✍🏻(Қысқа 2-3 сөзбен)")
    await test.next()


@dp.message_handler(state=test.q5)
async def ques4(message: types.Message, state=FSMContext):
    answer = message.text
    global ans4
    ans4 = answer
    await state.update_data(answer4=answer)


    data = await state.get_data()
    d_t = datetime.datetime.today()
    data_t = str(d_t)

    cursor.execute("INSERT INTO CLIENT (n, s, tele, data, type, c) VALUES(%s, %s, %s, %s, %s, %s)", (ans1, ans2, ans3, data_t, ans4, "false",))
    db.commit()

    '''
    cursor.execute("""
                   INSERT INTO design_employerr(
                                     first_name,
                                     last_name,
                                     telenumber,
                                     address,
                                     iin,
                                     H_P_F,
                                     education,
                                     status,
                                     reject,
                                     skills,
                                     true_false 
                   ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """, (ans1, ans2, ans3,  str(ans4), str(data_t), str(message.from_user.id)))
    conn.commit()

    '''




    await bot.send_message(message.from_user.id, "Жазған өтінішіңіз қабылданды😉\nЖақын уақытта компания қызметкерлері🤵🏽 сізбен хабарласады")
    await state.finish()




