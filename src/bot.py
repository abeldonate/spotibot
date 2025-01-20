import telebot
import os
from dotenv import load_dotenv
from spotify_parser import get_new_releases

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['new'])
def send_welcome(message):
    bot.reply_to(message, "These are the new releases from the artists you follow:" + str(get_new_releases()))

bot.infinity_polling()
