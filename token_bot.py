from aiogram import Bot, Dispatcher, types, executor
TOKEN = '6815995661:AAG2G2HpMtUjGoZC-HXxeeFin56Qnj10DA4'
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)