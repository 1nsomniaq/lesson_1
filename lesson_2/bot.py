# -*- coding: utf-8 -*-

import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = "760790871:AAH_R0rdywRkoOx_fz_wbdnyS_2aVhXX7pE"


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    logging.info('before_start')
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print text
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print user_text
    update.message.reply_text(user_text)

def get_constellation(bot, update):
    pass

main()
