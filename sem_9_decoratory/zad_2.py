"""Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов."""
from random import randint


def game_decorator(func):
    def wrapper(func_number, func_count):
        if not (100 >= func_number >= 1):
            func_number = randint(1,100)
        if not (10 >= func_count >= 1):
            func_count = randint(1, 10)
        func(func_number,func_count)
    return wrapper


@game_decorator
def game(number: int, count: int):
    print(number)
    print(count)
    nonlocal number, count
    for i in range(count):
        a = int(input('Введите число от 1 до 100:'))
        if a == number:
            print('Вы угадали')
            return i + 1
        elif a < number:
            print('Загаданное число больше.')
        else:
            print('Загаданное число меньше.')
