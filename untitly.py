from email import message
from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '5533453501:AAEf1sMwlvgudZIcUw4hcashL2IoyhPWbPU'
bot = telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Ассалому Алайкум, Хуш келибсиз!\nAssalomu Alaykum,Xush kelibsiz! "
    javob += "\nМатн киритинг:\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    #bot.reply_to(message, javob)
    bot.reply_to(message, javob(msg))

bot.polling()
