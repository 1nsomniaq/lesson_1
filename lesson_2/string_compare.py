# -*- coding: utf-8 -*-


def compare_string(string1, string2):
    if not (type(string1) == str and type(string2 == str)):
        return 0
    if string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3


assert compare_string(string1=1, string2='rfe') == 0
assert compare_string(string1=None, string2='rfe') == 0
assert compare_string(string1='', string2='rfe') is None
assert compare_string(string1='rfe', string2='rfe') == 1
assert compare_string(string1='f', string2='f') == 1
assert compare_string(string1='ff', string2='f') == 2
assert compare_string(string1='ff', string2='learn') == 3

