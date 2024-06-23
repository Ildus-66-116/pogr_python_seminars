"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
from string import ascii_letters


def del_symbol(my_str: str):
    """Удаляет все символы кроме латинский и переводит в нижний регистр"""
    res = ''
    for i in my_str:
        if i in ascii_letters or i == ' ':
            res += i
    return res.lower()


if __name__ == '__main__':
    print(del_symbol('My string 7, правда'))
