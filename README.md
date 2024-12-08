# Описание лабораторноц работы по Современным средства программирования
####  Создание телеграм-бота и дашборда с помощью обязательно нужных библиотек

# Необходимое для установки
1. Скачать ЯП Python c официального сайта здесь - [python](https://www.python.org/downloads/)
2. IDE для октыртия проект, это может быть [VSC](https://code.visualstudio.com/) или же [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows) выбирите на свой вкус, или же это может быть выбран другой IDE которого нет в нашем списке.
3. После скачивания всех нужного для установки, скачиваем все необходимое в репозитории.
4. Открываем IDE и в терминале устанавливаем нужные нам библиотеки.
-----------------------------
> Библиотеки для дашборда
* pip install dash
* pip install pandas
> Библиотека для бота
* pip install pyTelegramBotAPI
5. Установили библиотеки, запускаем проект.
6. Проверяем на работоспособность
-----------------------------
Язык программирования: __Python__
Среда разработки: __Pycharm__

 # Работоспособность бота
Бот отзывается по команде >/start
#### После чего, нам дают выбор между кнопок и если на них нажать 
* Контакты > Контакты фотостудии
* Аналитика > Ссылка на дашборд фотостудии
* Бронирование > Запись на фотосессию
* О нас > О фотостудии 

## Строчка кода
```
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
```

Цель проекта обеспечить удобное использование и поиска информации и обработка заявки на бронирование фотосесии
