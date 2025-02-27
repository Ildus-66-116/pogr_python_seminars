"""Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
import json
import os
from functools import wraps
from random import randint

def write_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        data_json = {}
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data_json = json.load(f)

        data_json[result] = {'args': args, **kwargs}

        with open(file_name, 'w') as f:
            json.dump(data_json, f)
        return result

    return wrapper


def count(number):
    def some_decorator(func):
        result = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(number):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return some_decorator


def game_decorator(func):
    @wraps(func)
    def wrapper(func_number, func_count):
        if not (100 >= func_number >= 1):
            func_number = randint(1, 100)
        else:
            func_number = randint(1, 100)
        if not (10 >= func_count >= 1):
            func_count = randint(1, 10)
        else:
            func_number = randint(1, 100)
        return func(func_number, func_count)

    return wrapper


@count(3)
@write_json
@game_decorator
def game(number, count):
    """Игра угадать число"""
    for i in range(count):
        a = int(input('Введите число от 1 до 100:'))
        if a == number:
            print('Вы угадали')
            return f'{number}, {i + 1}'
        elif a < number:
            print('Загаданное число больше.')
        else:
            print('Загаданное число меньше.')
    print(f'Вы не угадали, загаданное число было: {number}')
    return f'{number}, {0}'


print(game(98, 10))
