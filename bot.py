#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'вставьте_свой_токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий GitHub")
	item2 = types.KeyboardButton("😋 Написать мне в Telegram")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет, если ты QA то давай знакомиться, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/YakushinSar')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/AndreyYakushinSar')
		else:
			bot.send_message(message.chat.id, 'Пока! Хорошего дня! 😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
