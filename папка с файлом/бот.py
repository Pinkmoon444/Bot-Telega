import os

import html

# pip install requests
import requests

# pip install python-dotenv
from dotenv import load_dotenv

# pip install python-telegram-bot==13.7
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters



load_dotenv()
TOKEN = os.getenv("TOKEN")
бот = Bot(TOKEN)
# айдишник = 5622354606
# бот.send_message(chat_id=айдишник, text = "Бонжур")

def запарсить_погоду(город):
    ссылка = "https://www.google.com/search"
    параметры = {"q":f"погода в городе '{город} в градусах Цельсия'",'hl': 'ru'}
    # параметры позволяют нам сделать запрос более точным (то есть на русском, а не на татарско-итальянском)
    ответ_сайта = requests.get(ссылка, параметры)

    if ответ_сайта.status_code != 200:
        return "Сайт недоступен по неадекватной причине (Чертов гугл!)"
    текст = html.unescape(ответ_сайта.text)

    старт = текст.find("BNeawe tAd8D AP7Wnd")
    if старт == -1:
        return("Город не был распознан этим наишикарнейшим ботом")
    старт = текст.find(">", старт)
    старт += 1
    стоп = текст.find("<", старт)
    город = текст[старт:стоп]
    
    старт = текст.find("BNeawe iBp4i AP7Wnd")
    if старт == -1:
        return("Первый блок не найден")

    старт = текст.find("°C", старт)
    if старт == -1:
        return "Градусы не найдены."
    старт -= 15
    старт = текст.find(">", старт)
    старт += 1
    стоп = текст.find("<", старт)

    градусы = текст[старт:стоп]

    старт = текст.find("BNeawe tAd8D AP7Wnd", старт)
    if старт == -1:
        return("Второй блок не найден")
    старт = текст.find("\n", старт)
    старт += 1
    стоп = текст.find("<", старт)
    состояние_погоды = текст[старт:стоп].lower()
    return f"В городе {город} сейчас {градусы}, {состояние_погоды}"




def Отправить_Сообщение(айдишник, текст):
    бот.send_message(chat_id=айдишник, text = текст)
    

def реакция(информация, контекст):
#  эту функцию мы вызываем при получении нового сообщенияя. Ей обязатльно (автоматически) передаются два аргумента
    айди = информация._effective_message.chat_id
    # if айди == 5605127008:
        # Отправить_Сообщение(айди, "ЗА ТОБОЙ ОХОТИТСЯ ХЕРОБРИН")
        # return
    print(информация._effective_message.text)
    полученное_сообщение = информация._effective_message.text
    ответное_сообщение = f'Вы мне написали: "{полученное_сообщение}"'
    погода = запарсить_погоду(полученное_сообщение)
    Отправить_Сообщение(айди, погода)
    Отправить_Сообщение (айди, ответное_сообщение)


def запустить_бота():
    # класс updater позволяет слушать сервер телеграмма  и получать информацию о новых сообщениях
    обновление = Updater (TOKEN)
    обновление.dispatcher.add_handler(MessageHandler(Filters.text, реакция))
    # Dispetcher - распределяет нагрузку. ему нужны Handler (ы)
    # Add_handler - добавляет новый обработчик в список обработчиков диспетчера.
    # Massage handler - распределяет входяцие сообщения по разным функциям.
    # Filtes.text - Функция, которая будет вызвана при получении сообщения, которое совпадает с фильтром.

# зададим частоту опроса сервера (в секундах)
    обновление.start_polling(1)

    # Как только вызовется функия idle код будто-бы повиснет. ОН БУДЕТ БЕСКОНЕЧНО ОПРАШИВАТЬ СЕРВЕР ТЕЛЕГИ НА ПРЕДМЕТ входящих сообщений.
    обновление.idle()

запустить_бота()
