
# -*- coding: utf-8 -*-
import config
import telebot
import random
import requests
import time

bot = telebot.TeleBot(config.token)
@bot.message_handler(regexp='биткоин|биток')
def btc(message):
   req = requests.get('https://blockchain.info/ru/ticker').json()
   btc = req['USD']['last']
   bot.send_message(message.chat.id,"Хм... Спросим у Кери!")
   time.sleep(2)
   print(type(message.from_user.first_name))
   bot.send_message(message.chat.id,"Ну шо {}, биток уже {}$".format(message.from_user.first_name,btc))
   bot.send_sticker(message.chat.id, "CAADAgADGQADvKLSDVBmSmGAShnkAg")



@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
   if "мотив" in message.text.lower():
     bot.send_message(message.chat.id,config.citatki[random.randint(0,len(config.citatki)-1)])
   if message.from_user.first_name in config.lox:
       bot.send_message(message.chat.id, "Завали ебало валет!")
   if "парень который лидирует" in message.text.lower():
     bot.send_message(message.chat.id,"В данный момент лидер - Андрон")
   #if "/биткоин" in message.text.lower():
   #    bot.send_message(message.chat.id,"Такс такс такс, по данным Кирюхи биток щас %f $"%btc)

if __name__ == '__main__':
    bot.polling(none_stop=True)
