# -*- coding: utf-8 -*-


def ask_user():
    while True:
        user_answer = raw_input('Как дела?\n')
        if user_answer == 'Хорошо':
            break


def respond_to_user():
    question_to_answer_map = {"Как дела?": "Хорошо!",
                              "Что делаешь?": "Программирую"}
    while True:
        try:
            user_question = raw_input('Спроси что-нибудь.\n')
            print question_to_answer_map.get(user_question, 'Не умею на такое отвечать')
        except KeyboardInterrupt:
            print '\nПока!'
            break


if __name__ == '__main__':
    respond_to_user()
