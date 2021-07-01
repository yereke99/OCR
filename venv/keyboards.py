from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
import telegram_bot
from logger import dp, bot
from aiogram import types
from data_base import cursor, db

fi = open('resist_trimmer.pdf', 'rb').read()
files = open('z1.pdf', 'rb').read()
bugalteria = open('bugalteria.pdf', 'rb').read()

#
send_list_of_client = KeyboardButton('Документы')
send_check = KeyboardButton('Отчеты')
zayavka = KeyboardButton('Заявки')
send_list_of_clients = KeyboardButton('Документы сотрудников')

#start_button = ReplyKeyboardMarkup().row(send_check, send_list_of_clients, zayavka, send_list_of_clients)
start_button = ReplyKeyboardMarkup().add(send_list_of_client, send_check, zayavka, send_list_of_clients)
#

#
zayavka_employee = KeyboardButton('Книжка жалобов сотрудников')
zayavka_client = KeyboardButton('Заявка клиентов')
send_docs = KeyboardButton('Отправит документы')
z = ReplyKeyboardMarkup().add(zayavka_employee, zayavka_client, send_docs)
#


# Inline
inline_za = InlineKeyboardButton("Арыз-шағым🗣", callback_data='zayavka')
inline_mo = InlineKeyboardButton("Бухалтерия💵", callback_data='money')
inline_plan = InlineKeyboardButton("Пландар🗒", callback_data='plan')

inline = InlineKeyboardMarkup().add(inline_za, inline_mo, inline_plan)
#

# Inline 2
inline_docs = InlineKeyboardMarkup()
inline_send = InlineKeyboardButton("Қарау🕵🏻‍♂️", callback_data='look')
inline_receive = InlineKeyboardButton("қабылдау➡📁", callback_data='receive')
inline_docs.insert(inline_send)
inline_docs.insert(inline_receive)



@dp.callback_query_handler(text = 'zayavka')
@dp.callback_query_handler(text = 'money')
@dp.callback_query_handler(text = 'plan')
@dp.callback_query_handler(text = 'look')
@dp.callback_query_handler(text = 'receive')
async def pro(call: types.CallbackQuery):
    data = call.data

    if data == "zayavka":
        from sql2excell import _sql2excell
        _name = 'zayavki'
        _sql2excell(_name)
        string_name = open('{}.xlsx'.format(_name), 'rb').read()

        await bot.send_document(call.from_user.id, string_name)

        '''        try:
            cursor.execute("SELECT file_name FROM clients")
            public = cursor.fetchall()
            for filename in public:
                string = ''.join(filename)
                file_name = open('{}'.format(string), 'rb').read()
                await bot.send_document(call.from_user.id, file_name)


        except Exception as e:
            await bot.send_message(call.from_user.id, text='Мәліметтер базасында шағым жоқ')
        '''
    elif data == "look":
        try:
            cursor.execute("SELECT doc FROM DOCS")
            public = cursor.fetchall()
            for filename in public:
                string = ''.join(filename)
                file_name = open('{}'.format(string), 'rb').read()
                await bot.send_document(call.from_user.id, file_name)
        except Exception as e:
            await bot.send_message(call.from_user.id, text='Мәліметтер базасында документ жоқ')

    elif data == "receive":
        await bot.send_message(call.from_user.id, text='Құжатты жіберіңіз⬇')

    elif data == "money":
        await bot.send_document(call.from_user.id, bugalteria)
        await bot.send_document(call.from_user.id, fi)

    elif data == "plan":
        await bot.send_document(call.from_user.id, files)
        await bot.send_document(call.from_user.id, open('plan.pdf', 'rb').read())





        
