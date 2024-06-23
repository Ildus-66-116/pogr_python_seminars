"""Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV."""
import json
import csv
import os
from zad_2 import json_write

JSON_FILE_NAME = 'users.json'


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


def convert_dict_to_list(json_data):
    csv_data = []
    for level, value in json_data.items():
        for id, user_name in value.items():
            csv_data.append([level, id, user_name])
    return csv_data


def write_csv(file_name, csv_data):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f,  dialect='excel-tab')
        csv_write.writerows(csv_data)


def read_csv_dict(file_name):
    json_data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        csv_dict = csv.DictReader(f, dialect='excel-tab')
        for line in csv_dict:
            json_data.append(line)
    return json_data


def read_csv(file_name):
    csv_data = []
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        for line in csv.reader(f, dialect='excel-tab'):
            csv_data.append(line)
    return csv_data


def convert_csv_data(csv_data):
    for i in csv_data:
        i[1] = i[1].zfill(10)
        i.append(hash(i[1] + i[2]))
    return {i[-1]: i[:-1] for i in csv_data}


if __name__ == '__main__':
    # json_data = json_load('users.json')
    # print(json_data)
    # csv_data = convert_dict_to_list(json_data)
    # write_csv("csv_text.csv", csv_data)
    csv_data = read_csv('csv_text.csv')
    json_write('csv_json.json', convert_csv_data(csv_data))
