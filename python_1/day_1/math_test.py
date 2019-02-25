# Сложная задачка: создаем арифметический пример
# result = eval("2 + 4")  # вычисляет значение
# пока пользователь не ответит верно, подсчитываем
# кол-во ошибок
import random

wrong = 0
attempt = 0

while attempt != 5:
    digit_a = random.randint(0, 10)
    digit_b = random.randint(0, 10)
    correct_answer = digit_a * digit_b
    answer = input('Чему равно {a} * {b} = '.format(a=digit_a, b=digit_b))
    attempt = attempt + 1
    if answer.isdigit():
        answer = int(answer)
        if answer == correct_answer:
            print('Правильно, {}'.format(correct_answer))
        elif answer != correct_answer:
            wrong = wrong + 1
            print('{answer} Не правильно, будет {corr}.'.format(corr=correct_answer,
                                                                answer=answer))
    elif answer.isalpha():
        print('Что такое {}'.format(answer))

if wrong == 0:
    print('Супер, у тебя 5 правильных ответов из 5')
elif wrong == 1:
    print('Отлично, у тебя 1 неправильный ответ из 5')
elif wrong == 2:
    print('Хорошо, у тебя 2 неправильный ответа из 5')
elif wrong == 3:
    print('Плохо, у тебя 3 неправильный ответа из 5')
elif wrong == 4:
    print('Ужастно, у тебя 4 неправильный ответа из 5')
elif wrong == 5:
    print('Ты вообще учил?')
