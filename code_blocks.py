token = "925344997:AAGWfYn_GkgWBd1ViHdp6KcYmhG51yKSjJQ"


def make_conditions(response, request):
    condition = f'''
    if message.text.upper() == '{request}'.upper():
        bot.send_message(message.from_user.id, '{response}')'''
    return condition


# def text_response(text_res):
#     conditions = ''
#     for cond in text_res:
#         conditions += make_conditions(*cond)
#
#     body = f"""
# @bot.message_handler(content_types=['text'])
# def text_response(message):
#     {conditions}
#
#     """
#     return body

def text_response(res, req):
    conditions = ''
    for i in range(len(req)):
        conditions += make_conditions(res[i], req[i])

    body = f"""
@bot.message_handler(content_types=['text'])
def text_response(message):
    {conditions}

    """
    return body


def start_message(message):
    greetings = f'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "{message}")
    '''
    return greetings


start = f'''# -*- coding: cp1251 -*-

import telebot

token = '{token}'
bot = telebot.TeleBot(token=token)

'''

end = '''
bot.polling(none_stop=True, interval=0)
'''
text_res = []


# with open('main.py', 'a+') as f:
#     f.write(start)
#     text_res = [('hello', 'hello, my friend'), ('hi', 'hi, bitch')]
#     conditions = ''
#     for cond in text_res:
#         conditions += make_conditions(*cond)
#     f.write(text_response(conditions))
def bot_creating(res, req):
    with open('Instructions Example.txt', 'r') as instructions:
        with open('main.py', 'w+') as f:
            for line in instructions:
                if line.split()[0] == 'token':
                    token = line.strip()[1]
                elif line.split()[0] == 'start':
                    f.write(start)
                elif line.split()[0] == 'start_message':
                    f.write(start_message(line.strip().split('start_message')[1]))
                elif line.split()[0] == 'text_response':
                    text_res.append((line.split('\"\"')[1], line.split('\"\"')[3]))
                elif line.split()[0] == 'end':
                    pass
            f.write(text_response(res, req))
            f.write(end)
            #with open('main.py', 'w+') as f:
               # f.write(start)
               # f.write(start_message('Спасибо что запустил меня бро'))
              #  text_res = [('hello', 'hello, my friend'), ('hi', 'hi, bitch'), ('1+1', '2')]

              #  f.write(text_response(text_res))
              #  f.write(end)