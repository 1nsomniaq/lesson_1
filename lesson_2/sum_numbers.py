# -*- coding: utf-8 -*-
def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        raise Exception('оба аргумента должны быть числами')


assert get_summ('1', '2') == 3
assert get_summ(1, 1.1)
# assert get_summ('s', 1)
# assert get_summ(None, 4)
