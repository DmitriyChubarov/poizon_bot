from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Калькулятор стоимости', callback_data='calculator')],
    [InlineKeyboardButton('Отзывы', url='https://t.me/review_Poizon')],
    [InlineKeyboardButton('Помощь с заказом', callback_data='question')],
    [InlineKeyboardButton('Задать вопрос', url='https://t.me/sup_poizon')]
])

calc_keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Где найти цену в юанях?', callback_data='price_ua')],
    [InlineKeyboardButton('Калькулятор', callback_data='Summer_footwear')],
    [InlineKeyboardButton('Вернуться в меню', callback_data='back_to_menu')]
])

calc_keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Калькулятор стоимости', callback_data='calculator')],
    [InlineKeyboardButton('Вернуться в меню', callback_data='back_to_menu')]
])

calc_keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Ответы на вопросы', url='https://teletype.in/@poizon_streetwear/Otvety-na-voprosy')],
    [InlineKeyboardButton('Настройка фильтров/поиск по фото', url='https://teletype.in/@poizon_streetwear/Sortirovka_i_Filtrazia')],
    [InlineKeyboardButton('Как пользоваться Poizon', url='https://teletype.in/@poizon_streetwear/Kak-polzovatsa-Poizon')],
    [InlineKeyboardButton('Как выбрать карточку товара', url='https://teletype.in/@poizon_streetwear/Kak-vybrat-kartochku-tovara')],
    [InlineKeyboardButton('Вернуться в меню', callback_data='back_to_menu')]
])

calc_keyboard4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Ответы на популярные вопросы', callback_data='question')],
    [InlineKeyboardButton('Вернуться в меню', callback_data='back_to_menu')],
])

calc_keyboard5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Рассчитать ещё раз', callback_data='Summer_footwear')],
    [InlineKeyboardButton('Вернуться в меню', callback_data='back_to_menu')],
])