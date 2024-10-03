'''
телеграм логика
1. сделать функционал по сбору данных для просчёта прохода фрезы

'''

#import aiogram2, telebot

import telebot, asyncio
from telebot import types
import gpt_conferter

from telebot.types import (KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
# from bot_teleg_frezerovanie_gpt import logic_progod
import logic_progod

#TOKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA" #my_test_tutorial_bot

TOKEN="6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"#http://t.me/my_test_tutorial_bot

#TOKEN="6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ"

# TOKEN="6743802647:AAEUvXSAV7V6aMw4aoXI6PAqGB8dso8aV6o"#http://t.me/natyznoyp_potolok_bot

bot = telebot.TeleBot(TOKEN)


print("start", "остались проблемы переключения между гпт ботом не отлавливает")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расчитать проход")
    item2 = types.KeyboardButton("Расслабься")
    item3 = types.KeyboardButton("Спросить ИИ")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

# функция отбирает не верные данные если строка не может
# быть float
def func_otbor_float(dan1):
    list_sbor = ["0","1","2","3","4","5","6","7","8","9","."]
    new_str=""
    dan_str = str(dan1)
    dan_str = dan_str.replace(",", ".").lower()
    dan_str = dan_str.replace(" ", "")
    for znak in dan_str:
        if znak in list_sbor:
            new_str+=znak
    if new_str:
        return new_str
    else:
        return None

# глобальные перемены для работы с данными
danie_prohoda={}
name_prohod=None
name_prohod_eng = None

# основная фунция котороая работает с входящими данными
@bot.message_handler(
func=lambda message: message.text == "Расчитать проход")
def button_prohod(message):
    # global danie_prohoda
    # global name_prohod
    # global name_prohod_eng
    # danie_prohoda_list = []
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    paz = types.KeyboardButton("Рассчет паза")
    greben = types.KeyboardButton("Рассчет гребня")
    markup.add(paz, greben)
    bot.send_message(message.chat.id,
                     "Выберете что вам надо",
                     reply_markup=markup)


#отлов по пазу
@bot.message_handler(
        func=lambda message: message.text == "Рассчет паза")
def prohod_paza(message):
    global danie_prohoda
    global name_prohod
    global name_prohod_eng
    name_prohod = "паза"
    prohod = lambda x: x
    name_prohod_eng = prohod("paz")
    danie_prohoda[1]="Рассчет паза"
    bot.send_message(message.chat.id,
                    f"Учтите что диаметр фрезы должен быть меньше паза на 1мм."
                    f"Напишите диаметр фрезы в мм(ПРИМЕР 23.3)")


#отлов по гребню
@bot.message_handler(
        func=lambda message: message.text == "Рассчет гребня")
def prohod_grebna(message):
    global danie_prohoda
    global name_prohod
    global name_prohod_eng
    name_prohod = "гребня"
    prohod = lambda x: x
    name_prohod_eng = prohod("greben")
    bot.send_message(message.chat.id,
                     f"Напишите диаметр фрезы в мм(ПРИМЕР 23.3)")
    danie_prohoda[1]="Рассчет гребня"


#отлов всех флот даных
@bot.message_handler(#content_types in ["Расслабься", "Спросить ИИ"])
    func=lambda message:
    message.text not in ["Расслабься", "Спросить ИИ"])
def prohod_grebna_paz(message):
    global danie_prohoda
    global name_prohod
    global name_prohod_eng
    if len(danie_prohoda) == 1:
        # проверка ввода данных от ввода текстовых данных
        if func_otbor_float(message.text):
            danie_prohoda["freza"] = func_otbor_float(message.text)
            bot.send_message(message.chat.id,
                f"Напишите ширину {name_prohod} мм")
        else:
            bot.send_message(message.chat.id,
                f"Ошибочный ввод даных поробуйте заново")
    elif len(danie_prohoda) > 1:
        if func_otbor_float(message.text):
            danie_prohoda[name_prohod_eng] = func_otbor_float(message.text)
            # Ввод данных в класс
            ResuitProhoda = logic_progod.Result_Prohoda(
                otbr_func=danie_prohoda[1],
                frez=danie_prohoda["freza"],
                paz_greben=danie_prohoda[name_prohod_eng], )
            bot.send_message(message.chat.id,
                             f"Пойду посчитаю")
            danie_prohoda={}
            # отправляем данны для просчета логику расчета
            proxod = ResuitProhoda.prov_vxod()
            if proxod:
                bot.send_message(message.chat.id,
                     f"Сдвиг фрезы от 0 предчистовой"
                     f" {proxod['pred_chist_otr']} и "
                     f"{proxod['pred_chist_pol']} "
                     f"Сдвиг фрезы от 0 чистовой"
                     f" {proxod['chist_otr']} и "
                     f"{proxod['chist_pol']} ")
            elif proxod == None:
                bot.send_message(message.chat.id,
                    f"Диаметор фрезы больше ширины паза")
        # ошибочный ввод
        else:
            bot.send_message(message.chat.id,
                             f"Ошибочный ввод даных поробуйте заново")






# раслабься
@bot.message_handler(
func=lambda message: message.text == "Расслабься")
def porno_linc(message):
    bot.send_message(message.chat.id, 'http://porno365.scot')
    return
        

@bot.message_handler(
func=lambda message: message.text == "Спросить ИИ")
def work_ai(message):
    bot.send_message(message.chat.id,
                     "Напишите ваш вопрос")
    @bot.message_handler(
        func=lambda message: message.text != None)
    def message_reply(message):
        print("bot AI" , message.text)
        bot.send_message(message.chat.id,
            "Дайте мне несколько секунд")
        responce1 = asyncio.run(gpt_conferter.gpt3_text(message.text))
        if responce1:
            bot.send_message(message.chat.id, responce1)
        elif responce1 == "":
            bot.send_message(message.chat.id, "Повторите ваш вопрос")
            return
        #роабочий код




bot.infinity_polling()


