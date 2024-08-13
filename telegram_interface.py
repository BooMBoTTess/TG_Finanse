import Finance_module
import telebot
import dotenv
import Finance_module
from Classes import product
'''Телеграмм бот'''
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_TELEGRAMBOT = os.getenv('TOKEN_TELEGRAMBOT')
bot = telebot.TeleBot(TOKEN_TELEGRAMBOT)

#TODO: ниже
'''
QRRAW handler
QR handler
get_excel_file - достать эксельку
'''

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
		organisation_name, total_sum, DT, products = Finance_module.check_handler_QR(message.text, message.from_user, 1)
		message_template = f'Ваш чек от {organisation_name}, был послан {DT}:\n'
		for elem in products:
			message_template += f'{elem.name} - {elem.sum//100} руб.\n'
		bot.reply_to(message, message_template)


@bot.message_handler(content_types=['document', 'photo'])
def QR_code_handler(message):
	# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу
	file_name = message.document.file_name
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	with open(f'QR_buffer/{file_name}', 'wb') as new_file:
		new_file.write(downloaded_file)

	bot.reply_to(message, 'Приветик')

bot.polling(none_stop=True, timeout=123)