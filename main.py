from pyrogram import Client
from pyrogram.errors import FloodWait
from config import Config
from time import sleep

app = Client('my_account', api_id=Config.api_id, api_hash=Config.api_hash)
app.start()
alfa = []
try:
    for message in app.get_chat_history(app.join_chat(Config.invite).id, 2000):
        alfa.append(message)
except FloodWait as e:
    print(e)
    sleep(e.value)
    for message in app.get_chat_history(app.join_chat(Config.invite).id, 2000):
        alfa.append(message)
alfa = alfa[::-1]
for message in alfa:
    try:
        if message.text == None:
            continue
        print(f'Сообщение от {message.from_user.first_name}: {message.text}')
    except BaseException as e:
        continue
