"""module of buttons"""
from telebot import types


def hotel_buttons(letter : str):
    """ hotel buttons creating """
    keyboard = types.InlineKeyboardMarkup()
    hotel_1 = types.InlineKeyboardButton(text='Атлант', callback_data= letter + ' atlant')
    hotel_2 = types.InlineKeyboardButton(text='Атлант скай', callback_data=letter + ' atlant_sky')
    hotel_3 = types.InlineKeyboardButton(text='Корона', callback_data=letter + ' corona')
    hotel_4 = types.InlineKeyboardButton(text='Бумеранг', callback_data=letter + ' bumerang')
    hotel_5 = types.InlineKeyboardButton(text='Гавана', callback_data=letter + ' havana')
    hotel_6 = types.InlineKeyboardButton(text='Толассо', callback_data=letter + ' olasso')
    hotel_7 = types.InlineKeyboardButton(text='Мадрид парк', callback_data=letter + ' madrid_park')
    hotel_8 = types.InlineKeyboardButton(text='Орандж хаус', callback_data=letter + ' orange_house')
    hotel_9 = types.InlineKeyboardButton(text='Клевер', callback_data=letter + ' clever')
    hotel_10 = types.InlineKeyboardButton(text='Жемчужена заречя', \
        callback_data=letter + ' jemchujena')
    hotel_11 = types.InlineKeyboardButton(text='Буржуазия', callback_data=letter + ' burjuazia')
    hotel_12 = types.InlineKeyboardButton(text='другое', callback_data=letter + ' other')
    keyboard.add(hotel_1, hotel_2, hotel_3)
    keyboard.add(hotel_4, hotel_5, hotel_6)
    keyboard.add(hotel_7, hotel_8, hotel_9)
    keyboard.add(hotel_10, hotel_11, hotel_12)
    return keyboard


def tours_buttons(letter : str):
    """ tours buttons creating """
    keyboard = types.InlineKeyboardMarkup()
    tour_1 = types.InlineKeyboardButton(text='Золотое кольцо Абхазии', \
        callback_data=letter + ' zolotoye')
    tour_2 = types.InlineKeyboardButton(text='Крассная Поляна', callback_data=letter + ' kp')
    tour_3 = types.InlineKeyboardButton(text='Джип тур Абхазия', callback_data=letter + ' jeep')
    tour_4 = types.InlineKeyboardButton(text='33 водопада', callback_data=letter + ' vod33')
    tour_5 = types.InlineKeyboardButton(text='Обзорная по Сочи', callback_data=letter + ' sochi')
    tour_6 = types.InlineKeyboardButton(text='Квадрики', callback_data=letter + ' kvadrik')
    tour_7 = types.InlineKeyboardButton(text='Сплав', callback_data=letter + ' splav')
    tour_8 = types.InlineKeyboardButton(text='Джип тур Салахаул', callback_data=letter + ' salax')
    tour_9 = types.InlineKeyboardButton(text='Джип тур Псахо', callback_data=letter + ' psaxo')
    tour_10 = types.InlineKeyboardButton(text='Рыбалка', callback_data=letter + ' ryba')
    tour_11 = types.InlineKeyboardButton(text='Прогулка на яхте', callback_data=letter + ' yaxta')
    tour_12 = types.InlineKeyboardButton(text='Конные прогулки', callback_data=letter + ' kon')
    # tour_13 = types.InlineKeyboardButton(text='Другое', callback_data=letter + ' drug')
    keyboard.add(tour_1, tour_7)
    keyboard.add(tour_2, tour_8)
    keyboard.add(tour_3, tour_9)
    keyboard.add(tour_4, tour_10)
    keyboard.add(tour_5, tour_11)
    keyboard.add(tour_6, tour_12)
    # keyboard.add(tour_13)
    return keyboard


def finish_butttons(letter : str):
    """ finish button creating """
    keyboard = types.InlineKeyboardMarkup()
    yes_btn = types.InlineKeyboardButton(text='Да', callback_data=letter + ' yes')
    no_btn = types.InlineKeyboardButton(text='Нет', callback_data=letter + ' no')
    keyboard.add(yes_btn, no_btn)
    return keyboard


def edit_buttons(letter : str):
    """ edit button creating """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    name_btn = types.InlineKeyboardButton(text='Имя', callback_data=letter + ' name')
    tel_btn = types.InlineKeyboardButton(text='Номер телефона', callback_data=letter + ' tel')
    tour_btn = types.InlineKeyboardButton(text='Тур', callback_data=letter + ' tour')
    num_btn = types.InlineKeyboardButton(text='Количество взрослых', callback_data=letter + ' num')
    price_btn = types.InlineKeyboardButton(text='Цена', callback_data=letter + ' price')
    child_num_btn = types.InlineKeyboardButton(text='Количество детей',\
         callback_data=letter + ' child')
    child_price_btn = types.InlineKeyboardButton(text='Цена детского билета',\
         callback_data=letter + ' child_price')
    keyboard.add(tour_btn, num_btn, child_num_btn, child_price_btn, tel_btn, name_btn, price_btn)
    return keyboard


def otchet_buttons(letter : str):
    """ otchet button creating """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    all_hotels_btn = types.InlineKeyboardButton(text='Все отели',\
         callback_data=letter + ' all_hotels')
    one_hotel_btn = types.InlineKeyboardButton(text='Один отель', \
        callback_data=letter + ' one_hotel')
    keyboard.add(all_hotels_btn, one_hotel_btn)
    return keyboard


def edit_del_button(letter : str):
    """ finish button creating """
    keyboard = types.InlineKeyboardMarkup()
    del_btn = types.InlineKeyboardButton(text='Удалить', callback_data=letter + ' del')
    edit_btn = types.InlineKeyboardButton(text='Редактировать', callback_data=letter + ' edit')
    keyboard.add(del_btn, edit_btn)
    return keyboard
