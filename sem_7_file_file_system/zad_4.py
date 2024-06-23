"""✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""

from zad_2 import random_name
from random import randbytes, randint


def create_file(extension, min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    for i in range(1, file_count + 1):
        with open(f'dir_zad_4/{random_name(min_len, max_len)}_{i}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


create_file('txt', file_count=10)
