# -*- coding: utf-8 -*-
import random

MARKS = list(range(1, 6))
MAX_MARKS_LIST_LENGTH = 5


def get_marks():
    return [random.choice(MARKS) for _ in range(random.randint(0, MAX_MARKS_LIST_LENGTH))]


def get_grade():
    return str(random.choice(list(range(1, 12))))


def generate_school_marks_data():
    return [{'school_class': get_grade(), 'scores': get_marks()} for _ in range(3)]


def calculate_average(numbers_list):
    return sum(numbers_list) / float(len(numbers_list))


def calculate_average_mark(list_of_marks_by_school_class):
    school_marks = []
    for marks_in_class in list_of_marks_by_school_class:
        scores_list = marks_in_class['scores']
        if scores_list:
            average_mark_in_class = calculate_average(scores_list)
            print 'Средняя оценка в классе {0}:  {1:.2f}'.format(marks_in_class['school_class'], average_mark_in_class)
            school_marks.extend(scores_list)
    print 'Средняя оценка в школе: {0:.2f}'.format(calculate_average(school_marks))


school_marks_data = generate_school_marks_data()
calculate_average_mark(school_marks_data)
