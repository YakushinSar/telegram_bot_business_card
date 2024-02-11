#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'вставить токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Показать репозиторий GitHub")
	item2 = types.KeyboardButton("😋 Написать в Telegram")
	item3 = types.KeyboardButton("🧡 Показать своё резюме")


	markup.add(item1, item2)

	bot.send_message(message.chat.id, "{0.first_name} привет, если ты работаешь в сфере QA то давай знакомиться!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Показать репозиторий GitHub':
			bot.send_message(message.chat.id, 'https://github.com/YakushinSar')
		elif message.text == '😋 Написать в Telegram':
			bot.send_message(message.chat.id, 'https://t.me/AndreyYakushinSar')
		elif message.text == '🧡 Показать своё резюме':
			bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1sEmEBrTXDho7ovi9rqLp4lEjfMNUPsZn/view?usp=drive_link')
		else:
			bot.send_message(message.chat.id, 'Пока! Хорошего дня! 😢')


bot.polling(none_stop=True)










