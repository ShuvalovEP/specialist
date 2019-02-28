import os


def read_lines(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError as fnfe:
        print('Файл ненайден')
    except PermissionError as prme:
        print('Нет доступа к файлу на чтение')


if __name__ == '__main__':
    read_lines('file.txt')
