
# -*- coding: utf-8 -*-
import config
import telebot
import random
import requests
import time

bot = telebot.TeleBot(config.token)
@bot.message_handler(regexp='биткоин|биток|битку')
def btc(message):
   req = requests.get('https://blockchain.info/ru/ticker').json()
   btc = req['USD']['last']
   bot.send_message(message.chat.id,"Хм... Спросим у Кери!")
   time.sleep(2)
   bot.send_message(message.chat.id,"Ну шо {}, биток уже {}$".format(message.from_user.first_name,btc))
   bot.send_sticker(message.chat.id, "CAADAgADGQADvKLSDVBmSmGAShnkAg")



@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
   if "мотив" in message.text.lower().replace(" ", ""):
     bot.send_message(message.chat.id,config.citatki[random.randint(0,len(config.citatki)-1)])
   if message.from_user.first_name in config.lox:
       bot.send_message(message.chat.id, "Завали ебало валет!")
   if "беткоин" in message.text.lower().replace(" ", ""):
      bot.send_message(message.chat.id,"Ты шо вообще тупой? Какой беткоин?")
   if "парень который лидирует" in message.text.lower():
     bot.send_message(message.chat.id,"В данный момент лидер - Андрон")
   if "музыка тест" in message.text.lower():
     bot.send_voice(message.chat.id,"https://api.telegram.org/file/bot458426913:AAGSMe5Thm75vvDAHtqG95czDHKHzRqODuQ/topmuzon.com/files/music/russian/Lx24_-_Teryayu_Kontrol.mp3")
   
   #if "/биткоин" in message.text.lower():
   #    bot.send_message(message.chat.id,"Такс такс такс, по данным Кирюхи биток щас %f $"%btc)

if __name__ == '__main__':
    bot.polling(none_stop=True)
