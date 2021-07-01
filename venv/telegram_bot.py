from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from logger import dp, bot
from text import text_start, text_else, text_photo, image, error, text_
from keyboards import start_button, z, inline, inline_docs
import zayavka_cl, zayavki_za, zayavki_prostoe
from data_base import db, cursor
import datetime
from config import Token
import urllib.request

f = open('resist_trimmer.pdf', 'rb').read()
file_path = r'C:\Users\Yerek\PycharmProjects\new_system\venv\docs'

admin_id = 800703982
admin_new_id = 757709279

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print(message.from_user.id)
    if message.from_user.id == admin_id:
        await bot.send_message(message.from_user.id, text=text_start, reply_markup=start_button)
    else:
        u_id = message.from_user.id
        d_t = datetime.datetime.today()
        data_t = str(d_t)
        await bot.send_message(message.from_user.id, text=text_, reply_markup=z)

@dp.message_handler(content_types=['document'])
async def scan_message(msg: types.Message):
    document_id = msg.document.file_id
    file_info = await bot.get_file(document_id)
    fi = file_info.file_path
    name = msg.document.file_name
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{Token}/{fi}',f'./{name}')
    try:

        cursor.execute("INSERT INTO docs(doc) VALUES(%s)", (name,))
        db.commit()

        await bot.send_message(msg.from_user.id, 'Файл успешно сохранён')
    except  Exception as e:
        await bot.send_message(msg.from_user.id, 'Ошибка!')
    try:
        cursor.execute("INSERT INTO docs_from(file_name, data) VALUES(%s, %s)", (name, data_t,))
        db.commit()

        await bot.send_message(msg.from_user.id, 'Файл успешно сохранён')
    except  Exception as e:
        await bot.send_message(msg.from_user.id, 'Ошибка!')

@dp.message_handler(content_types=['text'])
async def public(message: types.Message):
    m = message.text
    if(m == "Документы"):
        await bot.send_message(message.from_user.id, text='Таңдаңыз😉', reply_markup=inline_docs)
    elif (m == "Отчеты"):
        await bot.send_message(message.from_user.id, text='Документтер кестесі📂', reply_markup=inline)
    elif (m == "Заявки"):
        await bot.send_message(message.from_user.id, text='Бұл жерде клиенттердің өтініштері🗣 келіп түседі')
        from sql2excell import sql_2_excell
        _name = 'zayavki_clientov'
        sql_2_excell(_name)
        string_name = open('{}.xlsx'.format(_name), 'rb').read()

        await bot.send_document(message.from_user.id, string_name)


    elif (m == "Документы сотрудников"):
        await bot.send_message(message.from_user.id, text='Бұл жерде компания қызметкерлері жіберген құжаттар тұрады!')
        cursor.execute("SELECT file_name FROM docs_from")
        files = cursor.fetchall()
        for file in files:
            filename = open('{}'.format(file), 'rb').read()
            await bot.send_document(message.from_user.id, filename)

    elif(m == "Книжка жалобов сотрудников"):
        await bot.send_message(message.from_user.id, text='Егер сіздің арыз-шығымыңыз🗣 болса /tap түймесін басыңыз🙃')

    elif (m == "Заявка клиентов"):
        await bot.send_message(message.from_user.id, text='Егер сіздің арыз-шығымыңыз🗣 болса /zay түймесін басыңыз🙃')

    elif m == '123147159':
        await bot.send_message(message.from_user.id, text='Құжатты жіберіңіз🗂')

    elif m == "Отправит документы":
        await bot.send_message(message.from_user.id, text='Компанияға жіберілетін документтерді жіберу ID еңгізіңіз✍🏻')

    else:
        await bot.send_message(message.from_user.id, text=text_else)






