import telebot
import time

from auth_data import token


# Initial main bot function
def telegram_bot(token):
    bot = telebot.TeleBot(token)

    # Bot hello message
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет ! Тут ты можешь узнать какие новые релизы вышли сегодня.')

    #
    @bot.message_handler(commands=['today'])
    def get_today_release(message):
        times = 0
        for i in get_releases():
            bot.send_message(message.chat.id, i)
            times += 1
            if times % 20 == 0:
                time.sleep(3)

    bot.polling()


if __name__ == '__main__':
    from main import *

    telegram_bot(token)
