# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное выражение.

from game_4 import riddle

_riddle_stat = {}


def stat_forming(riddle_text, attempt):
    if riddle_text in _riddle_stat:
        _riddle_stat[riddle_text].append(attempt)
    else:
        _riddle_stat[riddle_text] = [attempt]


def print_stat():
    for text, attempts in _riddle_stat.items():
        for item in attempts:
            print(f'Загадка {text}, отгадана с попытки {item}')


def riddle_game(riddle_dict):
    for key, value in riddle_dict.items():
        stat_forming(key, riddle(key, value, 3))


if __name__ == '__main__':
    riddle_dictionary = {'Зимой и летом одним цветом? 0': ['ель', 'елка', 'елочка'],
                         'Зимой и летом одним цветом? 1': ['ель', 'елка', 'елочка'],
                         'Зимой и летом одним цветом? 2': ['ель', 'елка', 'елочка']}
    riddle_game(riddle_dictionary)
    print_stat()
