# -*- coding: utf-8 -*-

user_age = raw_input('Введите возраст:\n')


def get_occupation_by_age(age_in_years):
    try:
        age_in_years = float(age_in_years.strip())
    except ValueError:
        raise Exception('Возраст должен быть числом')
    if age_in_years < 0:
        raise Exception('Возраст не может быть отрицательным')

    if age_in_years > 100:
        raise Exception('Слишком старый!')
    if age_in_years <= 7:
        return 'Детсадовец'
    elif age_in_years <= 18:
        return 'Школьник'
    elif age_in_years <= 23:
        return 'Студент'
    elif age_in_years <= 60:
        return 'Работник на работе'
    else:
        return 'Пенсионер'


print get_occupation_by_age(age_in_years=user_age)
