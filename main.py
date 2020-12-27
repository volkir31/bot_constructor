import telebot


token = '1234'
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def text_response(message):
    
    if message.text.upper() == 'hello'.upper():
        bot.send_message(message.from_user.id, 'hello, my friend')
    if message.text.upper() == 'hi'.upper():
        bot.send_message(message.from_user.id, 'hi, bitch')

    
bot.polling(none_stop=True, interval=0)
