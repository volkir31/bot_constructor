import telebot


token = '12314'
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def text_response(message):
    if message.text == '������'.upper():
        bot.send_message(message.from_user.id, '������. ��� � ���� ������?')
    if message.text == '����� ����������?'.upper():
        bot.send_message(message.from_user.id, '��-�� � 8:00 �� 20:00')
    
    
bot.polling(none_stop=True, interval=0)
