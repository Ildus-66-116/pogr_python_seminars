"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов."""

import pickle
from zad_2 import json_load


def pickle_writer(file_name, pickle_data):
    with open(file_name, 'wb') as f:
        pickle.dump(pickle_data, f)


def pickle_read(file_name):
    with open(file_name, 'rb') as f:
       return pickle.load(f)


if __name__ == '__main__':
    pickle_writer('pickle_test.pickle', json_load('csv_json.json'))
    print(pickle_read('pickle_test.pickle'))
