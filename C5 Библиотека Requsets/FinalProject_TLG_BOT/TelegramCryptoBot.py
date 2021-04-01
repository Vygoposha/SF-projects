import telebot
import requests
import json
from config import keys, TOKEN
from extensions import APIException, MoneyConverter


bot = telebot.TeleBot(TOKEN)

"""Клавиатура бота"""
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/start', '/help')


"""Вывод интсрукций по комадам"""
@bot.message_handler(commands=['start','help'])
def welcome_message(message):
    print(message)
    bot.send_sticker(message.chat.id,
                     'CAACAgUAAxkBAAPLYGRUs9q8Z6-0w_yoFSRNuIGIXtMAAoIDAALpCsgDjFkDselbxLceBA')
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}\n'
f'Чтобы использовать бот-ковертер введите данный в следующем формате:\n<имя валюты цену которой хотите узнать> '
f'<имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>\n'
f'Пример: Евро Рубль 1\n'
f'Чтобы увидеть список доступных валют, введите /values', reply_markup=keyboard1)

"""Вывод списка валют"""
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

"""Обработчик запросов"""
@bot.message_handler(content_types=['text',])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException("Нужно ввести 3 значения")
        symbols, base, amount = values
        # total_base = (json.loads(r.content)['rates'][keys[base]])
        total_base = MoneyConverter.get_price(symbols.lower(), base.lower(), amount.lower())
    except APIException as e:
        bot.reply_to(message, f"Ошибка ввода\n {e}")
    except Exception as e:
        bot.reply_to(message, f"Невозможно обработать команду\n {e}")
    else:
        text = f"{amount} {symbols.lower()}({keys[symbols.lower()]}) в {base.lower()}({keys[base.lower()]}) " \
               f"равен {int(amount)* total_base}"
        print(text)
        bot.send_message(message.chat.id, text)


"""не дает боту выключиться"""
bot.polling(none_stop=True)
