import telebot
from glob import glob
from PIL import Image
from dota2_data import all_charecters

from config import token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    charecters_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    charecters_keyboard.add('Juggernaut', 'Spectre', 'Axe', 'Abaddon', 'Lifestealer', 'Earth Spirit')
    bot.send_message(message.chat.id, 'персонажи', reply_markup=charecters_keyboard)

@bot.message_handler(content_types=['text'])
def send_message(message):
    #lists = glob('images/*')
    if message.text == 'Juggernaut':
        history = str(all_charecters['Juggernaut'])
        img = open('images/juggernaut.jpg', 'rb')

    elif message.text == 'Spectre':
        history = str(all_charecters['Spectre'])
        img = open('images/spectre.jpg', 'rb')

    elif message.text == 'Axe':
        history = str(all_charecters['Axe'])
        img = open('images/axe.jpeg', 'rb')

    elif message.text == 'Abaddon':
        history = str(all_charecters['Abaddon'])
        img = open('images/abaddon.jpg', 'rb')

    elif message.text == 'Lifestealer':
        history = str(all_charecters['Lifestealer'])
        img = open('images/lifestealer.jpg', 'rb')

    elif message.text == 'Earth Spirit':
        history = str(all_charecters['Earth Spirit'])
        img = open('images/earth_spirit.jpg', 'rb')

    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, history)

bot.polling()



