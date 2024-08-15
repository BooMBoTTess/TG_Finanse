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
	print('start', message.from_user.id)
	bot.reply_to(message, "Мурмур начали кушац")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Вот что ты хочешь спросить?")

@bot.message_handler(content_types=['text'])
def text_handler(message):
	print('text handler')
	if message.text[0:2] == 't=':
		print('qrraw')
		# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу
		response_code, response = Finance_module.check_handler_QR(message.text, message.from_user.id, 1)
		if response_code == 0:
			message_template = f'Ваш чек от {response["organisation"]}, был послан {response["datetime"]}:\n'
			for elem in response["products_list"]:
				message_template += f'{elem.name} - {elem.sum//100} руб.\n'
			bot.reply_to(message, message_template)
		elif response_code == -1:
			bot.reply_to(message, 'Не удалось найти чек по данному запросу')
		else:
			bot.reply_to(message, 'Неизвестная ошибка при исполнении программы')


@bot.message_handler(content_types=['photo'])
def QR_code_handler(message):
	# отправить в класс для работы. Класс должен вернуть ответ и выполнить всю работу
	file_info = bot.get_file(message.photo[0].file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	response_code, response = Finance_module.check_handler_QR(downloaded_file, message.from_user.id, 2)
	if response_code == 0:
		message_template = f'Ваш чек от {response["organisation"]}, был послан {response["datetime"]}:\n'
		for elem in response["products_list"]:
			message_template += f'{elem.name} - {elem.sum // 100} руб.\n'
		bot.reply_to(message, message_template)
	elif response_code == -1:
		bot.reply_to(message, 'Не удалось найти чек по данному запросу')
	else:
		bot.reply_to(message, response)


bot.polling(none_stop=True, timeout=123)