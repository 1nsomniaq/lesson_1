# -*- coding: utf-8 -*-

from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': u'Вася'},
    {'first_name': u'Петя'},
    {'first_name': u'Маша'},
    {'first_name': u'Маша'},
    {'first_name': u'Петя'},
]
print '\n'.join([': '.join([k, str(v)]) for k, v in Counter([student['first_name']
                                                             for student in students]).iteritems()])

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

print 'Самое частое имя среди учеников: {}'.format(
    max(Counter([student['first_name'] for student in students]).items(), key=lambda x: x[1])[0])

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print '\n'.join(['Самое частое имя в классе {}: {}'.format(index + 1, name) for index, name in
                 enumerate([max(Counter([student['first_name'] for student in students]).items(), key=lambda x: x[1])[0]
                            for students in school_students])])

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

print ' '.join(
    ['В классе {} {} девочки и {} мальчика.'.format(x[0], Counter(x[1]).get(False, 0), Counter(x[1]).get(True, 0)) for x
     in [(school_class['class'], [is_male[student['first_name']] for student in school_class['students']]) for
         school_class in school]])

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
