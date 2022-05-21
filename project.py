import telebot
import config
import requests
from telebot import types

bot = telebot.Telebot(config.token)

responce = requests.get(config.url).json()

bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.ReplyKeyboardMarkup('RUB')
    button2 = types.ReplyKeyboardMarkup('USD')
    button3 = types.ReplyKeyboardMarkup('EUR')
    markup.add(button1, button2,button3)
    mssg = bot.send_message(message.chat.id, 'Узнать курс валюты', reply_markup=markup)

    bot.register_next_step_handler(mssg, procces_coin_step)

def procces_coin_step (message, coin):
    try:
        markup = types.ReplyKeyboardMarkup(selecttive=False)

        for money in responce:
            if (message.next == coin('cvy')):
                bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']),
                       reply_markup=markup, parse_mode=('price'))

    except Exception as e:
        bot.reply_to(message, 'operator')

def printCoin(buy, sale):
    "Вывод курса"
    return "Курс продажи" + str(buy), "\n Курс покупки " + str(sale)

bot.enable_save_next_step_handler(delay=2)
bot.load_next_step_handler()

if __name__ == "__main__":
   bot.polling(none_stop=True)


