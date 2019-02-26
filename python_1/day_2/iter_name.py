# Получить список фамилий из файла  
# Выбрать самую длинную фамилию 

list_names = []
longest_last_name = ''
longest_last_name_to = ''
len_last_name = 0


obj = open('/Users/evgeny/Project/specialist/python_1/day_2/name.txt', 'r')

try:
    for name in obj:
        print('Фамилии из файла по очереди: ', name.strip())
        list_names.append(name.strip())
        if len(name) > len_last_name:
            len_last_name += len(name)
            longest_last_name = name
        elif len(name) >= len_last_name:
            longest_last_name_to = name
except IOError:
    print('Ошибка файла')

print('Содержимое list_names: ',list_names)


for name in list_names:
    count_tab = len_last_name - len(name)
    print('Фамилаия: ', count_tab * ' ', name)

print('Самая длинная фамилия: ', longest_last_name, longest_last_name_to)
