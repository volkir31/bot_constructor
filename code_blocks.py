token = 12314
start = f'''import telebot

token = '{token}'
bot = telebot.TeleBot(token=token)


'''
mess = 'привет'
response = 'Привет. Чем я могу помочь?'

condition = f"""if message.text == '{mess}':
        bot.send_message(message.from_user.id, '{response}')
"""
text_response = f"""@bot.message_handler(content_types=['text'])
def text_response(message):
    {condition}


"""


# bot.polling(none_stop=True, interval=0)

with open('main.py', 'a+') as f:
    f.write(start)
    f.write(text_response)

