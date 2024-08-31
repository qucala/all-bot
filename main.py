#!/usr/bin/python
from users import start
import telebot

API_TOKEN = 'token'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: message.text and message.text.lower() == '!all')
def tag_all_members(message):
    # Получаем информацию о чатеs
    s=''
    f=open('usernames.txt').readlines()
    for i in f:
        s+=i

    # Формируем сообщение с тегами
    tag_message = s
    
    
    # Отправляем сообщение с тегами
    bot.send_message(chat_id=message.chat.id,text=tag_message)
bot.polling()