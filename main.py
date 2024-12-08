from multiprocessing.connection import Client

import telebot
from aiohttp.web_fileresponse import content_type
from telebot import types
from aiogram.types import ReplyKeyboardMarkup, keyboard_button
bot = telebot.TeleBot('8195521689:AAErJkC-mgOTDICqXABkgJD45V3Phy9jxYE')

@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Нет', callback_data='no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Привет, это фотостудия Photolab, желаете узнать небольшую информацию про нас?', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_contacts = types.KeyboardButton('Контакты')
        item_analytics = types.KeyboardButton('Аналитика')
        item_reservation = types.KeyboardButton('Бронирование')
        item_information = types.KeyboardButton('О нас')
        markup_reply.add(item_contacts, item_analytics, item_reservation , item_information)
        bot.send_message(call.message.chat.id, 'Нажмите одну из кнопок', reply_markup=markup_reply)
    elif call.data == 'no':
        pass
        bot.send_message(call.message.chat.id, 'Хорошо, если у вас будут вопросы, просто напишите!')

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Контакты':
        bot.send_message(message.chat.id, 'Телефон: +7 (914) 444-77-77 '
        'Почта: orangedonelle@soscandia.org \
        Мы находимся по адресу: Город Комсомольск-на-Амуре, ул. Пушкина-Калатушкина д,  подъезд 2 этаж 3' )
    elif message.text == 'Аналитика'  :
        bot.send_message(message.chat.id, 'Вот, ты можешь перейти по ссылку и подробно разобраться '
        'http://127.0.0.1:8050/')
    elif message.text == 'О нас':
        bot.send_message(message.chat.id, 'Мы студия *PhotoLab* мы на рынке более 5-ти лет.')
    elif message.text == 'Бронирование':
        bot.send_message(message.chat.id,'Напишите дату, которое хотите забронировать')
    elif message.text == 'date' or 'month' or 'year':
        bot.send_message(message.from_user.id, 'Вы были записаны на фотостудию. Хорошего вам дня!')



bot.polling(none_stop=True, interval=0)


