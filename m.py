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

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
	
app = Client('admin', api_id=26251422, api_hash='d6cb852bdb66d574cc4b0b83dea37061')
	
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

 # Шаблон текста в строчки
@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>у них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я пропавший в dissmilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>из ниоткуда выйду в late</b>
	''')

	sleep(0.2)
	global number
	number = number + 1
	
	 # Шаблон текста в строчки 2
@app.on_message(filters.command("нсп", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	выебал
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	маму
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сын
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	свиноматки
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ебливой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	терпишь мой нон-стоп
	''')
	
		 # Шаблон текста в строчки 3
@app.on_message(filters.command("нсп1", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	где
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отпор
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	семихуюлинское
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отребье
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	этой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	конференции
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	которую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сто
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	раз
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нахаркали
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разбитую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	на две части
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	черепушку
	''')
	
	 # Шаблон текста в строчки 4
@app.on_message(filters.command("соси", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	засоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	усоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	присоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	дососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пересоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	насоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	подсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	надсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	всоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	обсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	изсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	не соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разсоси
	''')
	
	 # Шаблон текста в строчки 5
@app.on_message(filters.command("нсп2", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я тебя буду швырять телочку ебанную
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	окровавленный сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красную плесень
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твоей шизофренированной матери 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кинул как кость собаке
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кошу твое осознание и даже не стесняюсь
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	взорванный зачуханный дряблый сынуля куртизанки 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ты
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нашёл
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	себя
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	среди
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ярких
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красок
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	спермы?
	''')
	
	 # Шаблон текста в строчки 6
@app.on_message(filters.command("нсп3", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	червям приказ отдали потанцевать в твоём кишечнике
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	как те закрутка бутылки пива в кишечник моим великолепным нон стопом? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем путаешь бефидок с моей кончей и хуяришь его на завтрак? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я сигарету об твоё глазное яблоко тушу, теперь оно отслаивается
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ахихивхиххахип
	''') 
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я щас матери твоей кости распилю и дам тебе погрызть
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	скручивай ласты сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я тебе твое сасалище зарыганное в мясище разхуярил уже
	''')
	
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

@app.on_message(filters.sticker)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()

    if str(message.from_user.id) in usertoreply:
        with open('стик.txt', 'r+', encoding='utf-8') as file:
            alljokes = file.read().splitlines()
            randomjoke = random.choice(alljokes)
            message.reply(randomjoke)
            
@app.on_message(filters.command('xleb', prefixes='.') & filters.me)
async def valentine(app, message):
	global number
	await message.edit('⠀👩‍🦰          👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰         👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰💋👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶         👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶')
	sleep(0.2)
	await message.edit('*спустя 5 лет*')
	sleep(3)
	await message.edit('⠀👩‍🦰👶         👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶        👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶       👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶      👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶     👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶    👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶   👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶  👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞')

@app.on_message(filters.all)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()

    if str(message.from_user.id) in usertoreply:
        with open('пасты.txt', 'r+', encoding='utf-8') as file:
            alljokes = file.read().splitlines()
            randomjoke = random.choice(alljokes)
            message.reply(randomjoke)
        
print('хуй залупа')
app.run()
