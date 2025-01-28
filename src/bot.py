import telebot
import os
from dotenv import load_dotenv
from spotify_parser import get_new_releases
import time

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ME_ID = os.getenv('ME_ID')

bot = telebot.TeleBot(BOT_TOKEN)

# Parse the dict to a pretty message
def parse_message(message):
    parsed_message = ""
    for artist in message:
        parsed_message += f"\n{artist} released:\n"
        for album in message[artist]:
            parsed_message += f"- {album}\n"
    return parsed_message

while True:
     bot.send_message(ME_ID, "These are the new releases from the artists you follow:" + parse_message(get_new_releases()))
     time.sleep(60*60*24) # 24 hours

