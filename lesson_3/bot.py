# -*- coding: utf-8 -*-

import logging
import ephem
import datetime
import random
import re
from collections import defaultdict
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from cities import CITIES
from arithmetical_expression import ArithmeticalExpression, WrongArithmeticalExpression, NonBalancedParenthesis

OPERATIONS = '-+/*'


class WrongCityException(Exception):
    pass


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = "760790871:AAH_R0rdywRkoOx_fz_wbdnyS_2aVhXX7pE"

USED_CITIES = defaultdict(list)


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
    dp.add_handler(CommandHandler("wordcount", get_word_count, pass_args=True))
    dp.add_handler(CommandHandler("next_full_moon", get_next_full_moon, pass_args=True))
    dp.add_handler(CommandHandler("cities", get_city_for_game, pass_args=True))
    dp.add_handler(CommandHandler("calc", calculate_from_string, pass_args=True))

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


def get_word_count(bot, update, args):
    if not args:
        update.message.reply_text('Нужно было ввести строку для подсчета количества слов')
        return
    word_count = len(re.findall(r'[A-Za-z0-9]+', ' '.join(args)))
    update.message.reply_text('Количество слов: {}'.format(word_count))


def get_next_full_moon(bot, update, args):
    if not args:
        update.message.reply_text('Введите дату в формате:  гггг/мм/дд')
        return
    full_moon_dt = ephem.next_full_moon(datetime.datetime.strptime(args[0], '%Y/%m/%d'))
    update.message.reply_text('Ближайшее полнолуние: {}'.format(full_moon_dt))


def check_user_city(city_name, chat_id):
    if city_name not in CITIES:
        raise WrongCityException('Это точно город? Подумайте еще.')
    if city_name in USED_CITIES[chat_id]:
        raise WrongCityException('Кто-то из нас уже называл этот город')
    if USED_CITIES[chat_id] and city_name.lower()[0] != USED_CITIES[chat_id][-1]:
        raise WrongCityException(u'Вы играете не по правилам! Вам на \'{}\''.format(USED_CITIES[chat_id][-1][-1]))


def get_city_for_game(bot, update, args):
    chat_id = update.message.chat.id

    if not args:
        update.message.reply_text('Назовите город. Или сдаетесь? /cities new создаст новую игру.')
        return
    if args[0] == 'new':
        USED_CITIES[chat_id] = []
        update.message.reply_text('Ок, начнем все заново.')
        return

    user_city = args[0]
    try:
        check_user_city(city_name=user_city, chat_id=chat_id)
    except WrongCityException as exc:
        update.message.reply_text(exc.message)
        return

    compatible_cities = [city for city in CITIES if
                         city.lower()[0] == user_city[-1] and city not in USED_CITIES[chat_id]]
    if compatible_cities:
        next_city = random.choice(compatible_cities)
        update.message.reply_text(u'{}. Вам на \'{}\''.format(next_city, next_city[-1]))
        USED_CITIES[chat_id].extend([user_city, next_city])
    else:
        update.message.reply_text('Я сдаюсь!')
        USED_CITIES[chat_id] = []


def calculate_from_string(bot, update, args):
    if not args:
        update.message.reply_text('Надо было ввести арифметическое выражение')
        return
    user_string = ''.join(args)
    ar_exp = ArithmeticalExpression(user_string)
    try:
        ar_exp.check_syntax()
        ar_exp.check_parenthesis()
    except (WrongArithmeticalExpression, NonBalancedParenthesis) as exc:
        update.message.reply_text(exc.message)
        return
    ArithmeticalExpression.transform_to_postfix(ar_exp)
    result = ar_exp.calculate()
    update.message.reply_text(result)


main()
