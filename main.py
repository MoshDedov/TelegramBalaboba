from ctypes.wintypes import WORD
from email import message
import telebot;
import asyncio
import random
from aiobalaboba import balaboba
bot = telebot.TeleBot('1700854785:AAGK2qFUFaciMD-uQNiuwzH_48g4IP5DYEQ')


@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я-Балабоба, бот, способный составить целый текст из одного слова или фразы!\n\nЧтобы начать, напиши что-нибудь, а я продолжу.")
        bot.send_message(message.from_user.id, "Нейросеть не знает, что говорит, и может сказать всякое — если что, не обижайтесь. Распространяя получившиеся тексты, помните об ответственности.")
    elif message.text == "/info":
        bot.send_message(message.from_user.id, "Данный бот не претендует на замену оригинального решения компании Яндекс! Бот был создан в рамках школьного проекта ученика 9А класса Лицея №87 им.Л.И.Новиковой Молгачева Андрея.")
    elif message.text == "какой чай":
        bot.send_message(message.from_user.id, int(random.uniform(0, 30)))
    else:
        asyncio.run(get_balabobbed(message))


async def get_balabobbed(message):
    word = message.text
    # bot.send_message(message.from_user.id, "выбери стиль ответа:\n0 - Без стиля. По умолчанию.\n1 - Теории заговора.\n2 - ТВ-репортажи.\n3 - Тосты.\n4 - Пацанские цитаты.\n5 - Рекламные слоганы.\n6 - Короткие истории.\n7 - Подписи в Instagram.\n8 - Короче, Википедия.\n9 - Синопсисы фильмов.\n10 - Гороскоп.\n11 - Народные мудрости.\n18 - Новый Европейский Театр.")
    # style = int(message.text)
    response = await balaboba(word,)

    
    if word == response:
        bot.send_message(message.from_user.id, "давайте не ругаться, цивилизованные же люди...")
    else:
        bot.send_message(message.from_user.id, response)

bot.polling(none_stop=True, interval=0)
