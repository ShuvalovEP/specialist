import os
import time


def main():
    target = os.sys.argv[1]
    wait_time = int(os.sys.argv[2])
    while True:
        if os.path.exists(target):
            print(f'Каталог существует, каталог будет удален через: {wait_time} секунд')
            time.sleep(wait_time)
        else:
            os.makedirs(target)
            print(f'Создаю каталог {user_input_path}')


if __name__ == '__main__':
    main()
