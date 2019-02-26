# пишем бесконечный светофор
# программа пишет "на светофоре загорелся красный"
# стирает эту строку и пишет следующую

import sys
from time import sleep

lights = ['Красный', 'Желтый ', 'Зеленый']

while True:
    sys.stdout.write('Загорелся Желтый ')
    sys.stdout.flush()
    sleep(1)
    sys.stdout.write('\b' * 17)
    for light in lights:
        sys.stdout.write('Загорелся {}'.format(light))
        sys.stdout.flush()
        sleep(1)
        sys.stdout.write('\b' * 17)
