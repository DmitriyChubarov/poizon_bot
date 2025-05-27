from aiogram import Bot, Dispatcher, types, executor
from keyboards import main_keyboard
import calculator_all,what
from token_bot import dp, bot

@dp.message_handler(commands=['start'])
async def func_start(message: types.message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://ibb.co/q55W0K8',
                         caption='<b>Рады видеть тебя в нашем магазине!\nГлавное меню:</b>',
                         parse_mode="HTML",
                         reply_markup=main_keyboard)

calculator_all.register_hundler_calculator1(dp)
what.register_hundler_what1(dp)

async def start_mes(_):
    print('Бот был запущен!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=start_mes)


