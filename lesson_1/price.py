# -*- coding: utf-8 -*-


def format_price(price):
    price = int(price)
    return "Цена: %d руб." % price


display_price = format_price(price=56.24)
print display_price
