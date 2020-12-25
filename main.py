import telebot


token = '12314'
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def text_response(message):
    if message.text == 'привет'.upper():
        bot.send_message(message.from_user.id, 'Привет. Чем я могу помочь?')
    if message.text == 'какое расписание?'.upper():
        bot.send_message(message.from_user.id, 'ПН-ПТ с 8:00 до 20:00')
    
    
bot.polling(none_stop=True, interval=0)
