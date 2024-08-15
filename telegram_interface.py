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

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Мурмур начали кушац")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Вот что ты хочешь спросить?")

@bot.message_handler(content_types=['message'])
def text_handler(message):
	print('message handled')
	bot.reply_to(message, message.text)
	if message.text[0:1] == 't=':
		print('start QRraw')
		# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу
		response_code, response = Finance_module.check_handler_QR(message.text, message.from_user, 1)
		if response_code == 0:
			message_template = f'Ваш чек от {response["organisation"]}, был послан {response["datetime"]}:\n'
			for elem in response["products_list"]:
				message_template += f'{elem.name} - {elem.sum//100} руб.\n'
			bot.reply_to(message, message_template)
		elif response_code == -1:
			bot.reply_to(message, 'Не удалось найти чек по данному запросу')
		else:
			bot.reply_to(message, 'Неизвестная ошибка при исполнении программы')


@bot.message_handler(content_types=['document', 'photo'])
def QR_code_handler(message):
	print('DocorPhotohandled')
	# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу
	file_name = message.document.file_name
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	bot.reply_to(message, 'Приветик')

bot.polling(none_stop=True, timeout=123)