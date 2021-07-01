import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from  aiogram import Bot, types, Dispatcher
from config import Token

bot = Bot(token=Token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO,)