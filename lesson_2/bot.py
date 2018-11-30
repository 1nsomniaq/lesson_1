# -*- coding: utf-8 -*-

import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = "760790871:AAH_R0rdywRkoOx_fz_wbdnyS_2aVhXX7pE"


def get_planets_list():
    planets_list = []
    planets_and_moons = ephem._libastro.builtin_planets()
    for index, planet_type, planet_name in planets_and_moons:
        if planet_type == 'Planet':
            planets_list.append(planet_name)
    return planets_list


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    update.message.reply_text(user_text)


def get_constellation(bot, update, args):
    if not args:
        update.message.reply_text('Нужно было ввести название планеты после команды')
        return
    try:
        planet_name = args[0].title()
        planet = getattr(ephem, planet_name)()
    except AttributeError:
        update.message.reply_text('Такой планеты нет:( Введите одну из {}'.format(', '.join(get_planets_list())))
        return
    planet.compute()
    short_name, long_name = ephem.constellation(planet)
    update.message.reply_text(long_name)


main()
