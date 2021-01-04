token = 12314


def make_conditions(request, response):
    condition = f'''
    if message.text.upper() == '{request}'.upper():
        bot.send_message(message.from_user.id, '{response}')'''
    return condition


def text_response(conditions):
    body = f"""
@bot.message_handler(content_types=['text'])
def text_response(message):
    {conditions}

    """
    return body


start = f'''import telebot


token = '{token}'
bot = telebot.TeleBot(token=token)

'''

end = '''
bot.polling(none_stop=True, interval=0)
'''

with open('main.py', 'a+') as f:
    f.write(start)
    text_res = [('hello', 'hello, my friend'), ('hi', 'hi, bitch')]
    conditions = ''
    for cond in text_res:
        conditions += make_conditions(*cond)
    f.write(text_response(conditions))
    f.write(end)
