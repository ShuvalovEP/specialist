import os
import random


def path_file():
    work_path = '/Users/evgeny/Project/specialist/python_1/day_3/'
    file_name = 'en-ru.txt'
    return os.path.join(work_path, file_name)


def write_file(en, ru):
    text = f'{en}:{ru}\n'
    file = open(path_file(), 'a')
    file.write(text)


def revers_dict(lang='en'):
    dict_word = {}
    try:
        file = open(path_file(), 'r')
    except FileNotFoundError as fnf:
        print(f'Файл {path_file()} не найден')

    if lang == 'en':
        for i in file:
            list_word = i.split(':')
            dict_word.update({list_word[0]:list_word[1].strip()})
        return dict_word
    elif lang == 'ru':
        for i in file:
            list_word = i.split(':')
            dict_word.update({list_word[1].strip():list_word[0]})
        return dict_word


def find_word(word, lang='en'):
    dict_word = {}
    try:
        file = open(path_file(), 'r')
    except FileNotFoundError as fnf:
        print(f'Файл {path_file()} не найден')

    if lang == 'en':
        dict_word = revers_dict('en')
        return dict_word.get(word)
    elif lang == 'ru':
        dict_word = revers_dict('ru')
        return dict_word.get(word)


def lang_test(lang):
    wrong = 0
    attempt = 0
    dict_word = {}
    wrong_answer = {0:'     Супер,   у тебя 5 правильных ответов из 5',
                    1:'     Отлично, у тебя 1 неправильный ответ из 5',
                    2:'     Хорошо,  у тебя 2 неправильный ответа из 5',
                    3:'     Плохо,   у тебя 3 неправильный ответа из 5',
                    4:'     Ужастно, у тебя 4 неправильный ответа из 5',
                    5:'     Ты вообще учил?'}

    if lang == 'en':
        dict_word = revers_dict('en')
    elif lang == 'ru':
        dict_word = revers_dict('ru')

    while attempt != 5:
        question_id = random.choice(list(dict_word.keys()))
        correct_answer = dict_word.get(question_id)
        answer = input(f'Как переводится {question_id} ?: ')
        attempt = attempt + 1
        if answer == correct_answer:
            print(f'Правильно, {correct_answer}')
        elif answer != correct_answer:
            wrong = wrong + 1
            print(f'{answer} Не правильно, будет {correct_answer}')
    print(wrong_answer.get(wrong))


def main():
    while True:
        action = input('Пополнить, Найти или пройти Тест?: ')
        if action.lower() == 'пополнить':
            en = input('   Введите слово на английском: ')
            ru = input('   Введите слово на русском: ')
            write_file(en,ru)
            print(f'   Добавлено сочетание {en} - {ru}')
        elif action.lower() == 'найти':
            lang = input('   Какой язык (en или ru): ')
            word = input('   Введите искомое слово: ')

            print(f'"{word}" в переводе будет:' 
                if find_word(word, lang) is not None 
                else f'    "{word}" Ненайдено')
        elif action.lower() == 'тест':
            lang = input('   Какой язык (en или ru): ')
            lang_test(lang)


if __name__ == '__main__':
    main()
