import telebot

token = '12314'
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def text_response(message):
    if message.text == '������':
        bot.send_message(message.from_user.id, '������. ��� � ���� ������?')



