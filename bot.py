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


@bot.message_handler(commands=['pidor'])
def send_welcome(message):
    bot.send_message(message.chat.id, "генерирую пидора")
    time.sleep(2)
    bot.send_message(message.chat.id, "пидор - legkiy")

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

    if "мотив" in message.text.lower().replace(" ", ""):
        bot.send_message(message.chat.id, config.citatki[random.randint(0, len(config.citatki) - 1)])
    if message.from_user.first_name in config.lox:
        bot.send_message(message.chat.id, "Завали ебало валет!")
    if "беткоин" in message.text.lower().replace(" ", ""):
        bot.send_message(message.chat.id, "Ты шо вообще тупой? Какой беткоин?")
    if "парень который лидирует" in message.text.lower():
        bot.send_message(message.chat.id, "В данный момент лидер - Андрон")
    if "пидор" in message.text.lower():
        bot.send_message(message.chat.id, "генерирую пидора")
        time.sleep(2)
        bot.send_message(message.chat.id, "пидор - legkiy")
    if ("славаукраине" in message.text.lower().replace(" ","")) or ("славаукраїні" in message.text.lower().replace(" ","")):
         bot.send_message(message.chat.id, "Героям слава!!")
         bot.send_sticker(message.chat.id, "CAADAgADHAADMVD5DfMjhuKC0-w7Ag")
         bot.send_audio(message.chat.id, "https://upload.wikimedia.org/wikipedia/commons/transcoded/b/be/Anthem-of-Ukraine_Chorus_Veryovka.ogg/Anthem-of-Ukraine_Chorus_Veryovka.ogg.mp3",title="СЛАВА УКРАИНЕ")
if __name__ == '__main__':
    bot.polling(none_stop=True)
