# -*- coding: utf-8 -*-

import telebot
import os
from telebot import types

token = '925344997:AAGWfYn_GkgWBd1ViHdp6KcYmhG51yKSjJQ'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start_message(message):
   
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b0 = types.KeyboardButton("Кнопка 1")

    b1 = types.KeyboardButton("Не жми!")
    markup.add(b0,b1)

    bot.send_message(message.chat.id, " Hello, thanks for starting me".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def text_response(message):
    
    if message.text.upper() == '1 + 0'.upper():
        bot.send_message(message.from_user.id, '10')

    if message.chat.type == 'private':
        if message.text == 'Кнопка 1':
            bot.send_message(message.from_user.id, 'Ответ 1')    

        if message.text == 'Не жми!':
            bot.send_message(message.from_user.id, 'Ну просил же')    


bot.polling(none_stop=True, interval=0)
