# Дата и время в python
# Посчитать, когда вам исполнится 15000 дней
# узнать, сколько это будет полных лет

import datetime

now = datetime.datetime.now()
then = datetime.datetime(1986, 9, 25)
delta = then + datetime.timedelta(15000)

print('{day}.{month}.{year} Вам будет 15000 дней, это {old} год.'.format(year=delta.year,
                                                                         month=delta.month,
                                                                         day=delta.day,
                                                                         old=delta.year - then.year))
