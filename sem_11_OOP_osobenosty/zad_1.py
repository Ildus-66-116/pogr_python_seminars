"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
from datetime import datetime


class MyString(str):

    def __new__(cls, value, name_avtor, *args, **kwargs):
        instance = super().__new__(cls, value)
        return instance

    def __init__(self, value, name_avtor):
        self.name_autor = name_avtor
        self.time = datetime.now()

    def __str__(self):
        return f'Автор {self.name_autor} и время создание {self.time}'


if __name__ == '__main__':
    u_1 = MyString("a", 'Agata Kristi')
    print(u_1)
