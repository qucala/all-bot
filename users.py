import asyncio
from telethon import TelegramClient

# Укажите свои параметры API, которые вы получите на https://my.telegram.org
api_id = '*'
api_hash = '*'
group_name = '*'  # Замените на имя группы или используйте chat_id

# Создаем клиент
client = TelegramClient('session_name', api_id, api_hash)
s=[]
async def get_usernames():
    # Подключаемся к клиенту
    await client.start()

    # Получаем список диалогов (чаты, группы и т.д.)
    async for dialog in client.iter_dialogs():
        if dialog.name == group_name:  # Находим нужную группу по имени
            group = dialog
            break
    else:
        print("Группа не найдена")
        return

    # Получаем всех участников группы
    async for user in client.iter_participants(group):
        if user.username:
            s.append(f"@{user.username}")
        else:
            s.append(f"[{user.first_name}](tg://user?id={user.id})")
    return s
# Запускаем асинхронную функцию
def start():
    usernames=asyncio.run(get_usernames())
    # Открываем файл в режиме записи
    with open('usernames.txt', 'w', encoding='utf-8') as file:
        for username in usernames:
            if 'bot' not in username:
                file.write(username + '\n')

start()