def make_conditions(response, request):
    condition = f'''
    if message.text.upper() == '{request}'.upper():
        bot.send_message(message.from_user.id, '{response}')'''
    return condition


def make_button(name, message):
    names = ''
    button = f'''   
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
'''
    for i in range(len(name)):
        button += f'''
    b{i} = types.KeyboardButton("{name[i]}")
'''
    for i in range(len(name)):
        if i < len(name) - 1:
            names += 'b' + str(i) + ','
        else:
            names += 'b' + str(i)

    button += f'''    markup.add({names})
'''
    return button


def button_message(name, message):
    button_send_message = 'if message.chat.type == \'private\':'
    for i in range(len(name)):
        button_send_message += f'''
        if message.text == '{name[i]}':
            bot.send_message(message.from_user.id, '{message[i]}')    
'''
    button_send_message += '\n'
    return button_send_message


def text_response(res, req):
    conditions = ''
    for i in range(len(req)):
        conditions += make_conditions(res[i].strip(), req[i].strip())

    body = f"""

@bot.message_handler(content_types=['text'])
def text_response(message):
    {conditions}

    """
    return body


def start_message(message):
    greetings = f'''
    bot.send_message(message.chat.id, "{message}".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
    '''
    return greetings


def get_start(token):
    start = f'''import telebot
    
token = '{token}'
import os
from telebot import types

bot = telebot.TeleBot(token=token)
    
'''
    return start


onstart = '''@bot.message_handler(commands=['start'])
def start_message(message):
'''

end = '''
bot.polling(none_stop=True, interval=0)
'''

text_res = []
b_name = []
b_msg = []
res = []
req = []


def bot_creating(res, req, token, file_name):
    with open('Instructions Example.txt', 'r') as instructions:
        with open(file_name+'.py', 'w+') as f:

            f.write(onstart)

            for line in instructions:
                if line.split()[0] == 'token':
                    token = token
                elif line.split()[0] == 'start':
                    f.write(get_start(token))
                    f.write(onstart)
                elif line.split()[0] == 'make_button':
                    b_name.append(line.split('\"\"')[1])
                    b_msg.append(line.split('\"\"')[3])
                elif line.split()[0] == 'start_message':
                    on_start_msg = line.strip().split('start_message')[1]
                elif line.split()[0] == 'text_response':
                    req.append(line.split('\"\"')[1])
                    res.append(line.split('\"\"')[3])
                elif line.split()[0] == 'end':
                    pass
            f.write(make_button(b_name, b_msg))
            f.write(start_message(on_start_msg))
            f.write(text_response(res, req))
            f.write(button_message(b_name, b_msg))
            f.write(end)


bot_creating(res, req)

