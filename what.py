from aiogram import Dispatcher, types
from token_bot import dp, bot
from keyboards import calc_keyboard3,calc_keyboard4

async def question1(callback: types.callback_query):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='😉 Ответы на самые популярные вопросы уже ждут Вас.',
                           reply_markup=calc_keyboard3)

def register_hundler_what1(dp: Dispatcher):
    dp.register_callback_query_handler(question1, text='question')