import csv
import os
import re

file_path = '/Users/evgeny/Project/specialist/python_1/day_5'
file_name = 'bad.csv'
bad_csv = os.path.join(file_path, file_name) 


def get_data_csv():
    fields = ['date', 'name', 'eval']
    data_list = []
    with open(bad_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fields, delimiter=',')
        for row in reader:
            data_list.append(row)
    for line in data_list:
        print(line['date'], line['name'], line['eval'])

get_data_csv()

re.fullmath('[0-9]{4}') 