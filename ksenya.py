"""bot for ksenya"""
# import datetime
import os
import pandas as pd
import telebot
from telebot import types
from buttons import hotel_buttons, tours_buttons, finish_butttons, \
    edit_buttons, otchet_buttons, edit_del_button
import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    """ start command """
    start_btn(message)


@bot.message_handler(content_types=["text"])
def messages(message):
    """ message hendler """
    message1 = message.text

    if message1 == "новая заявка":
        new_order(message)

    elif message1 == "удалить заявку":
        del_order(message)

    elif message1 == "отчет":
        otchet(message)

    elif config.MESSAGE == "Num of persones":
        num_of_persones(message, message1)

    elif config.MESSAGE == "Price":
        price(message, message1)

    elif config.MESSAGE == "Num of child":
        child_num(message, message1)

    elif config.MESSAGE == "Price of child":
        child_price(message, message1)

    elif config.MESSAGE == "Date" :
        date(message, message1)

    elif config.MESSAGE == "Name":
        name(message, message1)

    elif config.MESSAGE == "Tel":
        tel(message, message1)

    elif config.MESSAGE == "Date promej":
        ochet_date(message, message1)

    elif config.MESSAGE == "else":
        else_message(message,message1)

    elif config.MESSAGE == "del date":
        del_edit_date(message, message1)

    elif config.MESSAGE == "del number":
        del_edit_num(message,message1)

    elif config.MESSAGE == 'edit name':
        edit_name(message,message1)

    elif config.MESSAGE == 'edit num':
        edit_num(message, message1)

    elif config.MESSAGE == 'edit tel':
        edit_tel(message, message1)

    elif config.MESSAGE == 'edit price':
        edit_price(message, message1)

    elif config.MESSAGE == 'edit child':
        edit_child(message, message1)

    elif config.MESSAGE == 'edit child_price':
        edit_child_price(message, message1)

    elif config.MESSAGE == 'hot other':
        other_hot(message, message1)

    elif config.MESSAGE == 'ostanovka':
        ostanovka(message, message1)


@bot.callback_query_handler(func=lambda call: call.data.startswith('f'))
def fin_btn(call):
    """ finish button """
    if call.data == "f yes":
        config.MESSAGE = "else"
        path = os.getcwd()
        path = os.path.join(path,"otchety")
        path = os.path.join(path, config.EXCEL_NAME)
        ex_name = config.DATE + ".xlsx"
        path = os.path.join(path, ex_name)
        data_frame = pd.read_excel(path)
        to_append = [config.TOUR, config.NUM_OF_PERSONS, config.PRICE, \
        config.CHILD_NUM, config.CHILD_PRICE,str(int(config.PRICE)*int(config.NUM_OF_PERSONS)\
        + int(config.CHILD_PRICE)*int(config.CHILD_NUM)), config.TEL_NUM, config.NAME \
        ,config.DATE]
        print(len(to_append))
        if config.HOTEL not in config.hotels:
            to_append.append(config.HOTEL)
        a_series = pd.Series(to_append, index = data_frame.columns)
        data_frame = data_frame.append(a_series, ignore_index=True)
        data_frame.to_excel(path, index= False)

        if config.CHILD_NUM == '0':
            text1 = config.DATE + "\n"  + config.OSTANOVKA + "\n"  +  \
                config.TOUR + '\n' + config.PRICE + "X" +  \
                config.NUM_OF_PERSONS + " = " + \
                str(int(config.PRICE)*int(config.NUM_OF_PERSONS)) + "\n" + \
                config.TEL_NUM + " " + config.NAME

        else:
            text1 = config.DATE + "\n" + config.OSTANOVKA + "\n" +  \
                config.TOUR + '\n' + config.PRICE + "X" +  \
                config.NUM_OF_PERSONS + "+" + config.CHILD_PRICE + "X" + config.CHILD_NUM + "="\
                + str(int(config.PRICE)*int(config.NUM_OF_PERSONS)\
                + int(config.CHILD_PRICE)*int(config.CHILD_NUM)) + "\n"  + \
                config.TEL_NUM + " " + config.NAME

        bot.send_message(call.message.chat.id , text= text1)

    elif call.data == "f no":
        bot.send_message(call.message.chat.id , text= "Нажмите на новую заявку")

@bot.callback_query_handler(func=lambda call: call.data.startswith('h'))
def hotels(call):
    """ hotels """
    keyb_tour = tours_buttons('t')

    if call.data == 'h atlant':
        config.HOTEL = "Атлант"
        config.OSTANOVKA = "Комсомолец"

    elif call.data == 'h atlant_sky':
        config.HOTEL = "Атлант скай"
        config.OSTANOVKA = "Мегафон"

    elif call.data == 'h corona':
        config.HOTEL = "Корона"
        config.OSTANOVKA = "Светофор"

    elif call.data == 'h bumerang':
        config.HOTEL = "Бумеранг"
        config.OSTANOVKA = "Южное Взморе"

    elif call.data == 'h havana':
        config.HOTEL = "Гавана"
        config.OSTANOVKA = "Южное Взморе"

    elif call.data == 'h tolasso':
        config.HOTEL = "Толассо"
        config.OSTANOVKA = "Комсомолец"

    elif call.data == 'h madrid_park':
        config.HOTEL = "Мадрид Парк"
        config.OSTANOVKA = "Пансионат Фригат"

    elif call.data == 'h orange_house':
        config.HOTEL = "Оранж Хаус"
        config.OSTANOVKA = "Сонатории Адлер"

    elif call.data == 'h clever':
        config.HOTEL = "Клевер"
        config.OSTANOVKA = "Пансионат Фригат"

    elif call.data == 'h jemchujena':
        config.HOTEL = "Жемчужина"
        config.OSTANOVKA = "Столовая южная"

    elif call.data == 'h burjuazia':
        config.HOTEL = "Буржуазия"
        config.OSTANOVKA = "Знания"

    elif call.data == 'h other':
        bot.send_message(call.message.chat.id, text="Выбирите другой отель")
        config.MESSAGE = "hot other"

    if call.data != 'h other':
        config.EXCEL_NAME = config.HOTEL
        config.TEXT = "Вы выбрали отель" + " " + config.HOTEL + " .\n"
        bot.send_message(call.message.chat.id , text= "Вы выбрали отель " + config.HOTEL)
        bot.send_message(call.message.chat.id, text="Выбырите тур" , reply_markup=keyb_tour)


@bot.callback_query_handler(func=lambda call: call.data.startswith('t'))
def tours(call):
    """ tours  """

    if call.data == 't zolotoye':
        config.TOUR = "Золотое кольцо Абхазии"

    elif call.data == 't kp':
        config.TOUR = 'Крассная Поляна'

    elif call.data == 't jeep':
        config.TOUR = 'Джип тур Абхазия'

    elif call.data == 't vod33':
        config.TOUR = '33 водопада'

    elif call.data == 't sochi':
        config.TOUR = 'Обзорная по Сочи'

    elif call.data == 't kvadrik':
        config.TOUR = 'Квадрики'

    elif call.data == 't splav':
        config.TOUR = 'Сплав'

    elif call.data == 't salax':
        config.TOUR = 'Джип тур Салахаул'

    elif call.data == 't psaxo':
        config.TOUR = 'Джип тур Псахо'

    elif call.data == 't ryba':
        config.TOUR = 'Рыбалка'

    elif call.data == 't yaxta':
        config.TOUR = 'Прогулка на яхте'

    elif call.data == 't kon':
        config.TOUR = 'Конные прогулки'

    config.TEXT = config.TEXT + "Вы выбрали тур " + config.TOUR + "."
    bot.send_message(call.message.chat.id , text= "Вы выбрали тур " + config.TOUR + ".")
    text2 = "Напишите сколько взрослых пойдут "
    config.MESSAGE = "Num of persones"
    bot.send_message(call.message.chat.id, text = text2)


@bot.callback_query_handler(func=lambda call: call.data.startswith('de'))
def del_or_edit(call):
    """ del or edit buttons """
    if call.data == "de del":
        config.DEL_EDIT = True
        config.TEXT = "Вы хотите удалить заявку"

    else:
        config.DEL_EDIT = False
        config.TEXT = "Вы хотите редактировать заявку"

    bot.send_message(call.message.chat.id, text=config.TEXT)
    keyb = hotel_buttons('dh')
    bot.send_message(call.message.chat.id, text="Выбирите отель", reply_markup=keyb)


@bot.callback_query_handler(func=lambda call: call.data.startswith('dh'))
def delete_hotels(call):
    """ delete order from base """
    if call.data == 'dh atlant':
        config.HOTEL = "Атлант"
        config.OSTANOVKA = "Комсомолец"

    elif call.data == 'dh atlant_sky':
        config.HOTEL = "Атлант скай"
        config.OSTANOVKA = "Мегафон"

    elif call.data == 'dh corona':
        config.HOTEL = "Корона"
        config.OSTANOVKA = "Светофор"

    elif call.data == 'dh bumerang':
        config.HOTEL = "Бумеранг"
        config.OSTANOVKA = "Южное Взморе"

    elif call.data == 'dh havana':
        config.HOTEL = "Гавана"
        config.OSTANOVKA = "Южное Взморе"

    elif call.data == 'dh tolasso':
        config.HOTEL = "Толассо"
        config.OSTANOVKA = "Комсомолец"

    elif call.data == 'dh madrid_park':
        config.HOTEL = "Мадрид Парк"
        config.OSTANOVKA = "Пансионат Фригат"

    elif call.data == 'dh orange_house':
        config.HOTEL = "Оранж Хаус"
        config.OSTANOVKA = "Сонатории Адлер"

    elif call.data == 'dh clever':
        config.HOTEL = "Клевер"
        config.OSTANOVKA = "Пансионат Фригат"

    elif call.data == 'dh jemchujena':
        config.HOTEL = "Жемчужина"
        config.OSTANOVKA = "Столовая южная"

    elif call.data == 'dh burjuazia':
        config.HOTEL = "Буржуазия"
        config.OSTANOVKA = "Знания"

    config.TEXT = config.TEXT + "\n" + "Заявку с отеля " + config.HOTEL
    bot.send_message(call.message.chat.id, text=config.TEXT)
    config.MESSAGE = "del date"
    bot.send_message(call.message.chat.id, text="Выбирите дату в формате (27.09,1.12)")


@bot.callback_query_handler(func=lambda call: call.data.startswith('df'))
def del_edit_finish(call):
    """ del edit finish """
    if call.data == 'df yes':
        path = os.getcwd()
        path = os.path.join(path,"otchety")
        path = os.path.join(path, config.HOTEL)
        ex_name = config.DATE + ".xlsx"
        path = os.path.join(path, ex_name)
        config.PATH = path
        df1 = pd.read_excel(path)

        if config.TEL_NUM in list(map(str,df1['Телефон'].tolist())):
            list_tel = list(map(str,df1['Телефон'].tolist()))
            ind = list_tel.index(config.TEL_NUM)
            config.IND = ind

            if config.DEL_EDIT:
                df1 = df1.drop(index=ind)
                df1.to_excel(path, index = False)
                bot.send_message(call.message.chat.id, text="Заявка удалена.")
                config.MESSAGE = 'else'

            else:
                config.NAME = df1.loc[config.IND].at['Имя']
                config.TOUR = df1.loc[config.IND].at['Тур']
                config.NUM_OF_PERSONS = df1.loc[config.IND].at['Кол. взр']
                config.PRICE = df1.loc[config.IND].at['Цена']
                config.CHILD_NUM = df1.loc[config.IND].at['Кол. детей']
                config.CHILD_PRICE = df1.loc[config.IND].at['Цена дет.']
                config.SUMMA = df1.loc[config.IND].at['Сумма']
                config.TEL_NUM = df1.loc[config.IND].at['Телефон']
                keyb = edit_buttons('dm')
                bot.send_message(call.message.chat.id, \
                    text="Выбирите что хотите редоктировать", reply_markup=keyb)

        else:
            bot.send_message(call.message.chat.id, text="Такого номера нету")
            config.MESSAGE = 'else'

    else:
        bot.send_message(call.message.chat.id , text= "Начните заново")
        config.MESSAGE = 'else'


@bot.callback_query_handler(func=lambda call: call.data.startswith('dm'))
def edit_red(call):
    """ editing data from base """
    if call.data == 'dm name':
        config.MESSAGE = 'edit name'
        bot.send_message(call.message.chat.id, text="Выбирите новое имя")

    elif call.data == 'dm tel':
        config.MESSAGE = 'edit tel'
        bot.send_message(call.message.chat.id, text="Выбирите новый номер телефона")

    elif call.data == 'dm tour':
        keyb = tours_buttons('dt')
        bot.send_message(call.message.chat.id, text="Выбирите новый тур", reply_markup=keyb)

    elif call.data == 'dm num':
        config.MESSAGE = 'edit num'
        bot.send_message(call.message.chat.id, text="Выбирите новое количество взрослых")

    elif call.data == 'dm price':
        config.MESSAGE = 'edit price'
        bot.send_message(call.message.chat.id, text="Выбирите новую цену взрослого билета")

    elif call.data == 'dm child':
        config.MESSAGE = 'edit child'
        bot.send_message(call.message.chat.id, text="Выбирите новое количество детей")

    elif call.data == 'dm child_price':
        config.MESSAGE = 'edit child_price'
        bot.send_message(call.message.chat.id, text="Выбирите новую цену за детский билет")


@bot.callback_query_handler(func=lambda call: call.data.startswith('dt'))
def edit_tour(call):
    """ edit tour """
    if call.data == 'dt zolotoye':
        config.TOUR = "Золотое кольцо Абхазии"

    elif call.data == 'dt kp':
        config.TOUR = 'Крассная Поляна'

    elif call.data == 'dt jeep':
        config.TOUR = 'Джип тур Абхазия'

    elif call.data == 'dt vod33':
        config.TOUR = '33 водопада'

    elif call.data == 'dt sochi':
        config.TOUR = 'Обзорная по Сочи'

    elif call.data == 'dt kvadrik':
        config.TOUR = 'Квадрики'

    elif call.data == 'dt splav':
        config.TOUR = 'Сплав'

    elif call.data == 'dt salax':
        config.TOUR = 'Джип тур Салахаул'

    elif call.data == 'dt psaxo':
        config.TOUR = 'Джип тур Псахо'

    elif call.data == 'dt ryba':
        config.TOUR = 'Рыбалка'

    elif call.data == 'dt yaxta':
        config.TOUR = 'Прогулка на яхте'

    elif call.data == 'dt kon':
        config.TOUR = 'Конные прогулки'

    bot.send_message(call.message.chat.id,text='Вы изменили тур на ' + config.TOUR)
    keyb = finish_butttons('di')
    bot.send_message(call.message.chat.id, text='Все верно??', reply_markup=keyb)


@bot.callback_query_handler(func=lambda call: call.data.startswith('di'))
def finish_edit(call):
    """ finish edit or no """
    if call.data == 'di yes':
        data_frame = pd.read_excel(config.PATH)
        data_frame = data_frame.drop(index = config.IND)
        config.SUMMA = str(int(config.NUM_OF_PERSONS)*int(config.PRICE) \
            + int(config.CHILD_PRICE)*int(config.CHILD_NUM))
        to_append =[config.TOUR, config.NUM_OF_PERSONS, config.PRICE, \
            config.CHILD_NUM, config.CHILD_PRICE, config.SUMMA, \
                config.TEL_NUM, config.NAME, config.DATE]
        a_series = pd.Series(to_append, index = data_frame.columns)
        data_frame = data_frame.append(a_series, ignore_index=True)
        data_frame.to_excel(config.PATH, index= False)

        if config.CHILD_NUM == '0':
            text1 = str(config.DATE) + "\n" + "Остановка " + \
                str(config.OSTANOVKA) + "\n" + "На " +  \
                config.TOUR + '\n' + str(config.PRICE) + "X" +  \
                str(config.NUM_OF_PERSONS) + " = " + \
                str(int(config.PRICE)*int(config.NUM_OF_PERSONS)) + "\n" + "Номер " + \
                str(config.TEL_NUM) + " " + str(config.NAME)

        else:
            text1 = str(config.DATE) + "\n" + "Остановка " +\
                 str(config.OSTANOVKA) + "\n" + "На " +  \
                str(config.TOUR) + '\n' + str(config.PRICE) + "X" +  \
                str(config.NUM_OF_PERSONS) + "+" + str(config.CHILD_PRICE) \
                    + "X" + str(config.CHILD_NUM) + "="\
                + str(int(config.PRICE)*int(config.NUM_OF_PERSONS)\
                + int(config.CHILD_PRICE)*int(config.CHILD_NUM)) + "\n" + "Номер " + \
                str(config.TEL_NUM) + " " + str(config.NAME)

        bot.send_message(call.message.chat.id, text=text1)
        config.MESSAGE = 'else'

    else:
        keyb = edit_buttons('dm')
        bot.send_message(call.message.chat.id, \
            text="Выбирите что хотите редоктировать", reply_markup=keyb)


@bot.callback_query_handler(func=lambda call: call.data.startswith('ol'))
def otchet_click(call):
    """ get otchet """
    if call.data == 'ol all_hotels':
        config.ALL_HOTEL = True
        bot.send_message(call.message.chat.id, text = "Выбирите дату (пример 27.09-28.09,1.9-1.10)")
        config.MESSAGE = "Date promej"

    elif call.data == 'ol one_hotel':
        config.ALL_HOTEL = False
        keyb_o_hot = hotel_buttons('oh')
        bot.send_message(call.message.chat.id, text="Выбырите отчет какого отеля хотите" , \
            reply_markup=keyb_o_hot)


@bot.callback_query_handler(func=lambda call: call.data.startswith('oh'))
def otchet_hotel(call):
    """ otchet hotel buttons """
    if call.data == 'oh atlant':
        config.HOTEL = "Атлант"

    elif call.data == 'oh atlant_sky':
        config.HOTEL = "Атлант скай"

    elif call.data == 'oh corona':
        config.HOTEL = "Корона"

    elif call.data == 'oh bumerang':
        config.HOTEL = "Бумеранг"

    elif call.data == 'oh havana':
        config.HOTEL = "Гавана"

    elif call.data == 'oh tolasso':
        config.HOTEL = "Толассо"

    elif call.data == 'oh madrid_park':
        config.HOTEL = "Мадрид Парк"

    elif call.data == 'oh orange_house':
        config.HOTEL = "Оранж Хаус"

    elif call.data == 'oh clever':
        config.HOTEL = "Клевер"

    elif call.data == 'oh jemchujena':
        config.HOTEL = "Жемчужина"

    elif call.data == 'oh burjuazia':
        config.HOTEL = "Буржуазия"

    bot.send_message(call.message.chat.id,\
        text = "Выбирите промежуток дат (пример 27.09-28.09,1.9-1.10)")
    config.MESSAGE = "Date promej"


@bot.callback_query_handler(func=lambda call: call.data.startswith('ok'))
def otchet_raz(call):
    """ otchet razvernutiy ili net """
    if call.data == 'ok yes':
        config.RAZVERNUT = True
        config.TEXT = config.TEXT + "\n" + "Развернутый отчет"

    elif call.data == 'ok no':
        config.RAZVERNUT = False
        config.TEXT = config.TEXT + "\n" + "Не развернутый отчет"

    bot.send_message(call.message.chat.id, text = config.TEXT)
    keyb = finish_butttons('of')
    bot.send_message(call.message.chat.id, text="Все верно?", reply_markup=keyb)


@bot.callback_query_handler(func=lambda call: call.data.startswith('of'))
def otchet_finish(call):
    """ otchet finish """
    if call.data == "of yes":
        df2 = pd.DataFrame()
        ind_of = config.DATE.index('-')
        start = config.DATE[:ind_of]
        stop = config.DATE[ind_of + 1:]
        ind_s = config.data.index(start)
        index_st = config.data.index(stop)
        path = os.getcwd()
        path_1 = os.path.join(path,'otchety')
        path_2 = os.path.join(path, 'output')

        if config.ALL_HOTEL:
            for j in config.hotels:
                df2 = pd.DataFrame()
                path1 = os.path.join(path_1, j)
                for i in range(ind_s,index_st+1):
                    path2 = os.path.join(path1,config.data[i])
                    file1 = path2 + '.xlsx'
                    df1 = pd.read_excel(file1)
                    df2 = df2.append(df1, ignore_index=True)
                df2 = df2.sort_values(by=['Тур', 'Дата'])
                path3 = os.path.join(path_2,j)
                file2 = path3 + '.xlsx'
                df2.to_excel(file2, index=False)

                if config.RAZVERNUT :
                    bot.send_document(call.message.chat.id,open(file2, 'rb'))

                else:
                    df3 = pd.read_excel(file2, \
                        usecols=['Тур', 'Кол. взр', 'Кол. детей', 'Сумма', 'Телефон', 'Имя'])
                    df3 = df3.groupby(by=['Тур']).sum()
                    df3.reset_index(inplace=True)
                    df3.to_excel(file2, index=False)
                    bot.send_document(call.message.chat.id,open(file2, 'rb'))


        else:
            path1 = os.path.join(path_1, config.HOTEL)
            for i in range(ind_s,index_st + 1):
                path2 = os.path.join(path1,config.data[i])
                file1 = path2 + '.xlsx'
                df1 = pd.read_excel(file1)
                df2 = df2.append(df1, ignore_index=True)
            df2 = df2.sort_values(by=['Тур', 'Дата'])
            path3 = os.path.join(path_2,config.HOTEL)
            file2 = path3 + '.xlsx'
            df2.to_excel(file2, index=False)

            if config.RAZVERNUT :
                bot.send_document(call.message.chat.id,open(file2, 'rb'))

            else:
                df3 = pd.read_excel(file2, \
                    usecols=['Тур', 'Кол. взр', 'Кол. детей', 'Сумма', 'Телефон', 'Имя'])
                df3 = df3.groupby(by=['Тур']).sum()
                df3.reset_index(inplace=True)
                df3.to_excel(file2, index=False)
                bot.send_document(call.message.chat.id,open(file2, 'rb'))

    else:
        bot.send_message(call.message.chat.id , text= "Начните заново")

def new_order(message):
    """ new order function """
    config.HOTEL = ""
    config.TOUR = ""
    config.OSTANOVKA = ""
    config.PRICE = 0
    config.NUM_OF_PERSONS = 0
    config.TEXT = ""
    config.TEL_NUM = 0
    config.NAME = ""
    config.DATE = ""
    config.DEL_HOTEL = ""
    config.ALL_HOTEL = True
    config.CHILD_NUM = 0
    config.CHILD_PRICE = 0
    config.MESSAGE = ""
    config.RAZVERNUT = True
    config.DEL_EDIT = True
    config.PATH = ""
    config.SUMMA = 0
    config.IND = 0
    config.EXCEL_NAME = ""
    keyb_hot = hotel_buttons('h')
    bot.send_message(message.from_user.id, text="Выбирите отель", reply_markup=keyb_hot)


def del_order(message):
    """ delete order function """
    config.HOTEL = ""
    config.TOUR = ""
    config.OSTANOVKA = ""
    config.PRICE = 0
    config.NUM_OF_PERSONS = 0
    config.TEXT = ""
    config.TEL_NUM = 0
    config.NAME = ""
    config.DATE = ""
    config.DEL_HOTEL = ""
    config.ALL_HOTEL = True
    config.CHILD_NUM = 0
    config.CHILD_PRICE = 0
    config.MESSAGE = ""
    config.RAZVERNUT = True
    config.DEL_EDIT = True
    config.PATH = ""
    config.SUMMA = 0
    config.IND = 0
    keyb = edit_del_button("de")
    bot.send_message(message.from_user.id, text="Выбирите что хотите делать", reply_markup=keyb)


def otchet(message):
    """ otchet funtction """
    config.HOTEL = ""
    config.TOUR = ""
    config.OSTANOVKA = ""
    config.PRICE = 0
    config.NUM_OF_PERSONS = 0
    config.TEXT = ""
    config.TEL_NUM = 0
    config.NAME = ""
    config.DATE = ""
    config.DEL_HOTEL = ""
    config.ALL_HOTEL = True
    config.CHILD_NUM = 0
    config.CHILD_PRICE = 0
    config.MESSAGE = ""
    config.RAZVERNUT = True
    config.DEL_EDIT = True
    config.PATH = ""
    config.SUMMA = 0
    config.IND = 0
    keyb_och = otchet_buttons('ol')
    bot.send_message(message.from_user.id, \
        text="Выбирите как хотите получить отчет", reply_markup=keyb_och)


def ostanovka(message,message1):
    """ ostanovka """
    config.OSTANOVKA = message1
    bot.send_message(message.chat.id, text="Вы выбрали остановку " + message1)
    keyb = tours_buttons('t')
    bot.send_message(message.chat.id, text="Выбирите тур", reply_markup=keyb)


def other_hot(message, message1):
    """ ochet hotel """
    config.EXCEL_NAME = 'другое'
    config.HOTEL = message1
    config.TEXT = "Вы выбрали отель " + config.HOTEL
    bot.send_message(message.chat.id,text="Вы выбрали отель " +\
         config.HOTEL + "\n Выбирите остановку")
    config.MESSAGE = 'ostanovka'


def name(message, message1):
    """ name function """
    message1 = message1.capitalize()
    config.NAME = message1
    config.TEXT = config.TEXT + "\n" + "Имя человека " + config.NAME + " ."
    bot.send_message(message.chat.id, text = "Имя человека " + config.NAME)
    bot.send_message(message.chat.id, text = "Напишите номер телефона.")
    config.MESSAGE = "Tel"


def num_of_persones(message, message1):
    """ num of person function """
    if message1.isdigit():
        config.NUM_OF_PERSONS = message1
        config.TEXT = config.TEXT + '\n' + "Поедут " + config.NUM_OF_PERSONS + " взр."
        bot.send_message(message.chat.id, text = "Поедут " + config.NUM_OF_PERSONS + " взр.")
        bot.send_message(message.chat.id, text = "Выбирите цену")
        config.MESSAGE = "Price"

    else:
        bot.send_message(message.chat.id, text="Выбирите количество взрослых (только цифры)")


def date(message, message1):
    """ date function """
    if message1 in config.data:
        config.DATE = message1
        config.TEXT = config.TEXT + '\n' + "Поедут в " + config.DATE + " числа."
        bot.send_message(message.chat.id, text = "Поедут в " + config.DATE + " числа.")
        bot.send_message(message.chat.id, text = "Выбирите имя")
        config.MESSAGE = "Name"

    else:
        bot.send_message(message.chat.id, \
            text="Выбирите дату (в формате 2.09, 1.12 от 1.09 до 31.12)")


def price(message, message1):
    """ price function """
    if message1.isdigit():
        config.PRICE = message1
        config.TEXT = config.TEXT + "\n" + 'Цена ' + config.PRICE + " руб."
        bot.send_message(message.chat.id, text = 'Цена ' + config.PRICE + " руб.")
        bot.send_message(message.chat.id, text = "Выбирите количество детей")
        config.MESSAGE = "Num of child"

    else:
        bot.send_message(message.chat.id, text="Выбирите цену на взрослый билет (только цифры)")


def child_num(message,message1):
    """ number of childes """
    if message1.isdigit():
        config.CHILD_NUM = message1

        if message1 != '0' :
            config.TEXT = config.TEXT + "\n" + "Поедут " + config.CHILD_NUM + " дет."
            bot.send_message(message.chat.id, text = "Поедут " + config.CHILD_NUM + " дет.")
            bot.send_message(message.chat.id, text = "Цену на детский билет")
            config.MESSAGE = "Price of child"
        else:
            bot.send_message(message.chat.id, text = "Выбирите дату (формат 27.09)")
            config.MESSAGE = 'Date'

    else:
        bot.send_message(message.chat.id, text="Выбирите количество детей (только цифры)")

def child_price(message, message1):
    """ price of childer """
    if message1.isdigit():
        config.CHILD_PRICE = message1
        config.TEXT = config.TEXT + '\n' + "Цена за детский билет " + config.CHILD_PRICE + " руб."
        bot.send_message(message.chat.id, text = "Цена за детский билет " \
            + config.CHILD_PRICE + " руб.")
        bot.send_message(message.chat.id, text = "Выбирите дату (формат 27.09)")
        config.MESSAGE = 'Date'

    else:
        bot.send_message(message.chat.id, text="Выбирите цену на детский билет (только цифры)")


def tel(message, message1):
    """ telephone number function """
    keyb_fin = finish_butttons('f')
    config.TEL_NUM = message1
    config.TEXT = config.TEXT + '\n' + "Номер телефона " + config.TEL_NUM + " ."
    bot.send_message(message.chat.id, text = config.TEXT)
    bot.send_message(message.chat.id, text="Все верно???" , reply_markup=keyb_fin)


def ochet_date(message, message1):
    """ ochet date """
    ind = message1.index("-")
    if message1[:ind] in config.data:
        keyb_och_fin = finish_butttons('ok')
        config.DATE = message1

        if config.ALL_HOTEL:
            config.TEXT = "Вы выбрали отчет для всех отелей на " + config.DATE + " дату."

        else:
            config.TEXT = "Вы выбрали отель " + config.HOTEL + " на " + config.DATE + " дату."

        bot.send_message(message.chat.id, text = config.TEXT)
        bot.send_message(message.chat.id, text="Развернутый отчет или нет???" ,\
            reply_markup=keyb_och_fin)

    else:
        bot.send_message(message.chat.id, \
            text="Выбирите дату (в формате 2.09, 1.12 от 1.09 до 31.12)")


def start_btn(message):
    """ start button """
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    new_call = types.KeyboardButton('новая заявка')
    delete_call = types.KeyboardButton('удалить/редактировать заявку')
    get_data = types.KeyboardButton('отчет')
    markup.add(new_call, delete_call, get_data)


    bot.send_message(message.from_user.id, text="Бот ждет", reply_markup=markup)


def del_edit_date(message, message1):
    """ del edit date """
    if message1 in config.data:
        config.DATE = message1
        config.TEXT = config.TEXT + "\n" + "На дату " + config.DATE
        bot.send_message(message.chat.id, text=config.TEXT)
        config.MESSAGE = "del number"
        bot.send_message(message.chat.id, text="Выбирите номер телефона")

    else:
        bot.send_message(message.chat.id, \
            text="Выбирите дату (в формате 2.09, 1.12 от 1.09 до 31.12)")



def del_edit_num(message, message1):
    """ del edit number """
    config.TEL_NUM = message1
    config.TEXT = config.TEXT + "\nНомер телефона " + config.TEL_NUM
    bot.send_message(message.chat.id, text = config.TEXT)
    keyb = finish_butttons("df")
    bot.send_message(message.chat.id, text = "Все верно??", reply_markup=keyb)


def edit_name(message, message1):
    """ edit name """
    message1 = message1.capitalize()
    config.NAME = message1
    keyb = finish_butttons('di')
    bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)


def edit_num(message, message1):
    """ edit number of persones """
    if message1.isdigit():
        config.NUM_OF_PERSONS = message1
        keyb = finish_butttons('di')
        bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)

    else:
        bot.send_message(message.chat.id, text="Выбирите количество взрослых (только цифры)")


def edit_child(message, message1):
    """ edit child number """
    if message1.isdigit():
        config.CHILD_NUM = message1
        keyb = finish_butttons('di')
        bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)

    else:
        bot.send_message(message.chat.id, text="Выбирите количество детей (только цифры)")


def edit_child_price(message, message1):
    """ edit child price """
    if message1.isdigit():
        config.CHILD_PRICE = message1
        keyb = finish_butttons('di')
        bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)

    else:
        bot.send_message(message.chat.id, text="Выбирите  цену детского билета (только цифры)")


def edit_price(message, message1):
    """ edit price """
    if message1.isdigit():
        config.PRICE = message1
        keyb = finish_butttons('di')
        bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)

    else:
        bot.send_message(message.chat.id, text="Выбирите цену взрослого билета (только цифры)")


def edit_tel(message, message1):
    """ edit telephone """
    config.TEL_NUM = message1
    keyb = finish_butttons('di')
    bot.send_message(message.chat.id, text='Все верно??', reply_markup=keyb)


def else_message(message, message1):
    """ else messasge"""
    bot.send_message(message.from_user.id, text="Бот ждет" + message1)


if __name__ == '__main__':
    bot.infinity_polling()
