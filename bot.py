import os
import telebot
from main import reverseAudioBuffer

BOT_TOKEN = os.environ.get('BOT_TOKEN')
INPUT_FILE_NAME = 'original.ogg'
OUTPUT_FILE_NAME = 'reversed.ogg'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey, send me an audio message and I will reply to you with reversed one")

@bot.message_handler(func=lambda message: True, content_types=['audio', 'voice'])
def echo_all(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    output_file = reverseAudioBuffer(downloaded_file)
    bot.send_voice(message.chat.id, telebot.types.InputFile(output_file))

bot.infinity_polling()