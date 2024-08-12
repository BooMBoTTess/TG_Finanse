import Finance_module
import telebot
import dotenv
'''Телеграмм бот'''

TOKEN = ''
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['message'])
def text_handler(message):
	bot.reply_to(message, message.text)
	if message.text[0:1] == 't=':
		# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу

@bot.message_handler(content_types=['document', 'photo'])
def photo_handler(message):
	bot.reply_to(message, 'QR код был отправлен')
	# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу

bot.polling(none_stop=True, timeout=123)