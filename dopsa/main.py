import telebot
from telebot import types
import random

from config import config
from menegers import generate_array


data = {}
count_win = 0
bot = telebot.TeleBot(config["token"], parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Welcome message
    Функция которая срабатывает при запуске бота или вызове команд /start, /help

    Args:
        message
    """
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/student')
    itembtnv = types.KeyboardButton('/start')
    markup.add(itembtna, itembtnv)  # создаём кнопочки меню

    data[message.chat.id] = 0  # создаём пользователя в нашей системе
    bot.send_message(message.chat.id, "Привет, Допсяш! Я глупый и не понимаю контекст сообщений, поэтому "
                                      "используй команды из списка 👇", reply_markup=markup)


@bot.message_handler(commands=['student'])
def send_welcome(message):
    """Generate message
    Функция, которая при вызове команды /student,
    делает следующий шаг
    и отправляет сообщение о прогрессе пользователя

    Args:
        message
    """
    global count_win
    if data[message.chat.id] == 6:
        data[message.chat.id] = 0
        name = message.chat.first_name
        count_win += 1
        text = f"{name} помог(ла) убежать студенту от допсы! 🏆\n\nОн закрыл сессию уже {count_win} раз!\n\n🥴💯💯💯💯💯💯💯🧑🏼‍💻🥂"
        bot.send_message(message.chat.id, text)
        return  # выходим из функции, так как дальнейшие шаги нас не интересуют
    if random.random() >= 0.2:
        data[message.chat.id] += 1
        text = "Студент) на шаг ближе к закрытию сессии!🥳"
    else:
        data[message.chat.id] = 0
        text = "Студент попал на допсу, начинаем заново.🥴"

    progress = generate_array(data[message.chat.id])
    bot.send_message(message.chat.id, f"{text}\n\n{progress} 🥂")


bot.infinity_polling()
