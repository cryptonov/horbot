# -*- coding: utf-8 -*-
import config
import telebot
import random

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    print(message)
    if "мотивац" in message.text.lower():
      bot.send_message(message.chat.id,config.citatki[random.randint(0,len(config.citatki))])
    if message.from_user.first_name in config.lox:
        bot.send_message(message.chat.id, "Завали ебало валет!")



if __name__ == '__main__':
    bot.polling(none_stop=True)