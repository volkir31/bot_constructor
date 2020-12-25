token = 12314
count_condition = 2
start = f'''import telebot


token = '{token}'
bot = telebot.TeleBot(token=token)


'''
mess = ['привет', 'какое расписание?']
response = ['Привет. Чем я могу помочь?', 'ПН-ПТ с 8:00 до 20:00']


def make_condition(message, response):
    condition = f"""if message.text == '{message}'.upper():
        bot.send_message(message.from_user.id, '{response}')
    """
    return condition

condition = ''
for i in range(count_condition):
    me = mess[i]
    res = response[i]
    condition += make_condition(me, res)

body = f"""@bot.message_handler(content_types=['text'])
def text_response(message):
    {condition}
    
"""


end = '''bot.polling(none_stop=True, interval=0)
'''


with open('main.py', 'a+') as f:
    f.write(start)
    f.write(body)
    f.write(end)

