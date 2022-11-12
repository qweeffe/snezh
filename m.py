import random
import pickle
import asyncio
from time import sleep
from random import shuffle
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import FloodWait
import textwrap
import os
import json
import pickle
import time
from math import ceil

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
	
app = Client('admin', api_id=26251422, api_hash='d6cb852bdb66d574cc4b0b83dea37061')
	

def parting(xs, parts):
    part_len = ceil(len(xs)/parts)
    return [xs[part_len*k:part_len*(k+1)] for k in range(parts)]
    
#сасно да? как и хуй даркова
HELP = '''
-/ХУЙ ДАРКОВА??/-
| .help - услуги даркова?)?)))?)?)
| .пасты [NUMBER] - отправить [NUMBER] паст, по умолчанию 1
| .new [TEXT] - добавить новую пасту
| .ghoul - вычитаем с тысячи семь вплоть до -1
| .spam [NUMBER] [TEXT] - ну кто не понял, тому скину деньги на лечение
| .нсп[NUMBER (1-3)] - максимальное количество нсп на данный момент [3]
| .соси - типикал хуйня от даркова
| .type - передвижение спермы даркова по тексту
'''

if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

@app.on_message(filters.command('c', prefixes='.') & filters.me)
def send_words(_, message):
    text = message.text.split(" ", 2)
    num = int(text[1])
    words = text[2].split()
    words_mass = parting(words, num)
    for words_to_send in words_mass:
        group_words = ""
        for word in words_to_send:
            message.delete()
            group_words=(f"{group_words} {word}")
        
        app.send_message(message.chat.id, group_words)

#паста хуяста
@app.on_message(filters.command("пасты", prefixes=".") & filters.all)
def past(_, message):
    alreadyUse = []
    message.delete()

    with open('пасты.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        
    jokescouht = len(lines)

    try:
        count = int(message.text.split()[1])
    except:
        count = None


    if count:
        if not count > jokescouht:
            for number in range(count):
                while True:
                    word = random.choice(lines)
                    if not word in alreadyUse:
                        app.send_message(message.chat.id, f'{word}')
                        sleep(0.5)
                        alreadyUse.append(word)
                        break
        else:
            app.send_message(message.chat.id, f'ты че ебанутый/ая? у меня есть только {jokescouht}')
    else:
        word = random.choice(lines)
        app.send_message(message.chat.id, word)

#помощь нахуй
@app.on_message(filters.command("help", prefixes=".") & filters.all)
def help(_, message):
    message.delete()
    app.send_message(message.chat.id, HELP)

# нью паста
@app.on_message(filters.command("add", prefixes=".") & filters.me)
def add(_, message):
    message.delete()
    newJoke = message.text.split('.add ')[1]
    with open('пасты.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{newJoke}')
    message.edit('успешно!')
    time.sleep(1)
    message.delete()

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) 

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)
	
#рандомайзер
@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'

#1000-7
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)

#спамер
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number

	if not spams:
		msg.edit(f'''
			**Error: Что-то пошло не так...\nИспользование: .spam <кол-во спама> <слово>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

#правда/ложь
@app.on_message(filters.command("tf", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[правда]", "[ложь]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: Вы не ввели вопрос!\nИспользование: .tf <вопрос>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1		
	
@app.on_message(filters.command('adduser', prefixes='.') & filters.me)
def adduser(_, message):
    id = message.text.split('.adduser ')[1]
    if '@' in id:
        id = app.get_users(id).id

        with open('userlist.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{id}\n')

        message.edit(f'{id} Добавлен!')

    else:
        try:
            with open('userlist.txt', 'a+', encoding='utf-8') as file:
                file.write(f'{int(id)}')

            message.edit(f'{id} Добавлен!')
        except:
            message.edit('ID может быть числом или пингом!')


@app.on_message(filters.command('deluser', prefixes='.') & filters.me)
def deluser(_, message):
    id = message.text.split('.deluser ')[1]

    if '@' in id:
        id = app.get_users(id).id

    with open('userlist.txt', 'r', encoding='utf-8') as file:
        allids = file.read().splitlines()
        if str(id) in allids:
            allids.remove(str(id))

            open('userlist.txt', 'w').close()
            with open('userlist.txt', 'a', encoding='utf-8') as file:
                for idtowrite in allids:
                    file.write(f'{int(idtowrite)}\n')

            message.edit(f'{id} Удалён!')
        else:
            message.edit(f'{id} не существует!')

@app.on_message(filters.command('id', prefixes='.') & filters.me)
def id(_, message):
    message.edit(f'ID = {message.reply_to_message.from_user.id}')

@app.on_message(filters.command('id', prefixes='.') & filters.me)
def id(_, message):
    message.edit(f'ID = {message.reply_to_message.from_user.id}')

# @app.on_message(filters.sticker)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()

    if str(message.from_user.id) in usertoreply:
        with open('стик.txt', 'r+', encoding='utf-8') as file:
            alljokes = file.read().splitlines()
            randomjoke = random.choice(alljokes)
            message.reply(randomjoke)

@app.on_message(filters.text)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()
        kew = ["1"]
        kew1 = random.choice(kew)
        
    if str(message.from_user.id) in usertoreply:
        with open('пасты.txt', 'r+', encoding='utf-8') as file:
            if kew1 in "1":
                alljokes = file.read().splitlines()
                randomjoke = random.choice(alljokes)
                message.reply(randomjoke)
        
print('хуй залупа')
app.run()
