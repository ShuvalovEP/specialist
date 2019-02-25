age = input('Введите ваш возраст: ')

if age.isdigit():
    age = int(age)
    if age <= 3:
        print('Вы сидите дома')
    elif age > 3 and age <= 6:
        print('Вам пора в садик')
    elif age > 6 and age <= 17:
        print('Вам пора в школу')
    elif age > 17 and age <= 22:
        print('Вам пора в институт')
    elif age > 22 and age <= 25:
        print('Вам пора в аспирантуру')
    elif age > 25 and age <= 59:
        print('Вам пора на работу')
    elif age > 60:
        print('Пора на дачу, Ва пенсионер')
    else:
        print('Ого, а это как?')
else
    print('Возраст необходимо указать простым числом')
