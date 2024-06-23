"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки."""
import json

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.readlines()
    text_dict = {}
    for item in text:
        key, value = item.strip().split(' | ')
        key = key.title()
        if key in text_dict:
            text_dict[key].append(value)
        else:
            text_dict[key] = [value]
    return text_dict

def write_json(file_name, json_data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


json_data = read_file('zad_mult_1')
write_json('zad1_json', json_data)


