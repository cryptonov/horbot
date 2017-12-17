# -*- coding: utf-8 -*-
import config
import telebot
import random
import json
import urllib2

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    print(message)
    req = urllib2.Request("https://blockchain.info/ru/ticker")
    opener = urllib2.build_opener()
    f = opener.open(req)
    js = json.loads(f.read())
    print(json)
    if "мотив" in message.text.lower():
      bot.send_message(message.chat.id,config.citatki[random.randint(0,len(config.citatki)-1)])
    if message.from_user.first_name in config.lox:
        bot.send_message(message.chat.id, "Завали ебало валет!")
    if "парень который лидирует" in message.text.lower():
      bot.send_message(message.chat.id,"В данный момент лидер - Андрон")
   # if "/биткоин" in message.text.lower():
   #    bot.send_message(message.chat.id,"Такс такс такс, по данным Кирюхи биток щас %f $"%btc)



if __name__ == '__main__':
    bot.polling(none_stop=True)
