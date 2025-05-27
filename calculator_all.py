from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from token_bot import dp, bot
from keyboards import calc_keyboard1, calc_keyboard2, main_keyboard, calc_keyboard5
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


#@dp.callback_query_handler(text='calculator')
async def calculator_main(callback: types.callback_query):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='📊Калькулятор для рассчета стоимости товаров разбит по категориям.\nКаждая категория отличается по весу ⚖️, который влияет на стоимость доставки 🚚\nКалькулятор рассчитывает стоимость товара с доставкой до склада в России. \n🚚Доставка по России до Вашего пункта выдачи оплачивается <b>ОТДЕЛЬНО.</b>\n❗️Для заказа нескольких позиций, просто сложите все расчеты вместе.',
                           parse_mode='HTML',
                           reply_markup=calc_keyboard1)

async def calculator_price(callback: types.callback_query):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='😊Чтобы рассчитать стоимость товара правильно, пожалуйста, придерживайтесь инструкции.\n\n❗️В приложении POIZON стоимость товаров зависит от размера.')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/wS0t6bg',
                         caption='Открыв карточку товара нажимаем "бирюзовую" кнопку для выбора размера.')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/r5qxtbb',
                         caption='Выбираем нужный размер и снова жмем по бирюзовой кнопке.\n\nВыкуп в приложении POIZON осуществляется <b>исключительно по бирюзовой кнопке</b>.',
                         parse_mode='HTML')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/DzC9g3Y',
                         caption='Теперь убираем все скидочные купоны. Жмем по скидке чтобы открыть окно выбора купонов.\n\nК сожалению, скидочные купоны доступны для новых пользователей, так как наша команда выкупает товары ежедневно мы их не имеем.')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJrpnEoKCXHNXdy6qN3vIY9f8dR0y7HSSJ58TB0OJGoA&s',
                         caption='Не работает картинка почему то\nНа выбранном купоне убираем галочку, чтобы купон стал неактивным.')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/gwFFdqT',
                         caption='После того как купон стал неактивным жмем по бирюзовой кнопке для просмотра окончательной цены.')
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/5FnCN1c',
                         caption='Теперь когда купоны неактивны Вы можете увидить конечную стоимость товара, по которой будет совершен выкуп.\n\nКонечная стоимость отмечена на скриншоте стрелочками.',
                         reply_markup=calc_keyboard2)

async def back_menu(callback: types.callback_query):
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo='https://ibb.co/q55W0K8',
                         caption='<b>Рады видеть тебя в нашем магазине!\nГлавное меню:</b>',
                         parse_mode="HTML",
                         reply_markup=main_keyboard)


#Расчет цены
class FSM_S_F(StatesGroup):
    S_F = State()

async def price1(callback: types.callback_query):
    await FSM_S_F.S_F.set()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Введите стоимость товара в юанях.\nНапример: 555')

async def price_1(message: types.message, state: FSMContext):
    if message.text.isdigit():
        b = 1000 + (12*int(message.text))
        await message.reply(f'Стоимость вашего товара без учёта доставки {b} рублей.\nЦена доставки 1050 руб/кг, для уточнения писать @sup_poizon',
                            reply_markup=calc_keyboard5)
        await state.finish()
    else:
        await message.answer('Это не число')

def register_hundler_calculator1(dp: Dispatcher):
    dp.register_callback_query_handler(calculator_price, text='price_ua')
    dp.register_callback_query_handler(calculator_main, text='calculator')
    dp.register_callback_query_handler(back_menu, text='back_to_menu')
    dp.register_callback_query_handler(price1, text='Summer_footwear', state=None)
    dp.register_message_handler(price_1, state=FSM_S_F.S_F)
