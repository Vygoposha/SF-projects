import telebot

""""Создание бота по токену"""
TOKEN = '1777211184:AAGdMf1iiwQRbmGZXODZbctucjRZOcwRmDY'
bot = telebot.TeleBot(TOKEN)

"""Параметры клавиатуры"""
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/start', '/help')


#
# @bot.message_handler()
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")

#  Получает к консоль id стикера
@bot.message_handler(content_types=['sticker'])
def repeat(message: telebot.types.Message):
    print(message)

# Обратабывает получаемое изображение
@bot.message_handler(content_types=['photo'])
def handle_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

# Обрабатываются все сообщения содержащие команды '/start'
@bot.message_handler(commands=['start'])
def welcome_message(message):
    print(message)
    bot.send_sticker(message.chat.id,
                     'CAACAgIAAxkBAAN5YF3SzwABlfSTjfqwBiAsO5I3JJcUAAIRAAMkkdUWpAsjJ-_a-6geBA')
    bot.send_message(message.chat.id, f'Приветсвую тебя, {message.from_user.first_name}'
                                      f'\nСовсем скоро это бот научится выбирать того, '
                                      f'кто будет забивать чаху сегодня')

# Обрабатываются все сообщения содержащие команду '/help'
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Себе помоги', reply_markup=keyboard1)

#  Обрабатывает текстовые сообщения, отвечает по ключевому слову
@bot.message_handler(content_types='text')
def handle_DR(message: telebot.types.Message):
    if message.text.lower() == "кто не поздравил влада с др?":
        bot.send_message(message.chat.id, "Пидоры Леха и Денис")
    elif message.text.lower() == "кто главный пидор?":
        bot.send_message(message.chat.id, 'Конечно же Леха')
    elif message.text.lower() == "кто будет забивать чаху?":
        bot.send_message(message.chat.id, "Леха")




bot.polling(none_stop=True)