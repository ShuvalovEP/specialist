# Кассир.
# Спрашивает, нужен ли пакет, есть ли дисконтная карта.
# Если пакет нужен к сумме покупок прибавлять 2 рубля. 
# Если есть дисконтная карта, делаем скидку 3% с суммы покупок 
# Если введена пустая строка, закрываем чек выводим сумму покупок


while True:
    discount_card = 0
    shopping_bag = 0
    discount = 0
    price = 0
    count = 0
    shopping_bag = input('Здравствуйте, Вам пакетик нужен? ')
    discount_card = input('Социальная карта или карта магазина есть? ')

    while price != '':
        price = input('Цена товара: ')
        if price.isdigit():
            count += int(price)
        elif price.isalpha():
            print('Не понимаю что такое {}, введите пожалуйста число'.format(price))

    if price == '':
        if shopping_bag.lower() == 'да':
            count = count + 2
        if discount_card.lower() == 'да':
            discount = count * 3 / 100
            count = count - discount
        print('С вас {} руб.\n\nСледующий'.format(count))
