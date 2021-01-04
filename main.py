# -*- coding: cp1251 -*-

import telebot

token = '925344997:AAGWfYn_GkgWBd1ViHdp6KcYmhG51yKSjJQ'
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, " Hello, thanks for starting me")


@bot.message_handler(content_types=['text'])
def text_response(message):
    if message.text.upper() == '1 + 0'.upper():
        bot.send_message(message.from_user.id, '10')


bot.polling(none_stop=True, interval=0)
