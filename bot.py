# -*- coding: utf-8 -*-
import config
import telebot
import random
import requests
import time
from bs4 import BeautifulSoup as BS
#298424523

bot = telebot.TeleBot(config.token)


@bot.message_handler(regexp='биткоин|биток|битку')
def btc(message): 
    req = requests.get('https://blockchain.info/ru/ticker').json()  
    btc = req['USD']['last'] 
    bot.send_message(message.chat.id, "Хм... Спросим у Кери!")  
    time.sleep(2) 
    bot.send_message(message.chat.id, "Ну шо {}, биток уже {}$".format(message.from_user.first_name, btc)) 
    bot.send_sticker(message.chat.id, "CAADAgADGQADvKLSDVBmSmGAShnkAg")
    


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(commands=['music'])
#def send_music(message):
    #songName = message.text[7:].replace(" ","+")
   # print(songName)
  #  str = "http://mp3party.net/search?q={}".format(songName)
   # print(str)
  #  if len(songName) == 0 :
  #      bot.send_message(message.chat.id, "Функция находится в бете. Введите /music имя трека для поиска")
#        return
 #   req = requests.get(str)
 #   soup = BS(req.content,'html.parser')
 #   songList = soup.find('div',{'class':'song-item'})
  #  if type(songList) == type(None):
 #       bot.send_message(message.chat.id,"Трек не найден. Попробуй еще раз(иногда помогает)")
 #       return
 #   realSong ={}
 #   realSong['href'] = songList.find('a')['href']
#   realSong['name'] = songList.find('a').text
 #   str = "http://mp3party.net"+realSong['href']
 #   req = requests.get(str)
 #   soup = BS(req.content,'html.parser')
 #   link = soup.find('div',{'class','download'}).find('a')['href']
#    print(type(link))
 #   bot.send_audio(message.chat.id, link,title=realSong['name'])


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    print(message)
    if "мотив" in message.text.lower().replace(" ", ""):
        bot.send_message(message.chat.id, config.citatki[random.randint(0, len(config.citatki) - 1)])
    if message.from_user.first_name in config.lox:
        bot.send_message(message.chat.id, "Завали ебало валет!")
    if "беткоин" in message.text.lower().replace(" ", ""):
        bot.send_message(message.chat.id, "Ты шо вообще тупой? Какой беткоин?")
    if "парень который лидирует" in message.text.lower():
        bot.send_message(message.chat.id, "В данный момент лидер - Андрон")








if __name__ == '__main__':
    bot.polling(none_stop=True)
