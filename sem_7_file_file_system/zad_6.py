"""✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""

from zad_2 import random_name
from random import randbytes, randint
from pathlib import Path
import os


def create_file(extension, path='dir_zad_4', min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    path_exist(path)
    for i in range(1, file_count + 1):
        file_name = os.path.join(path, random_name(min_len, max_len)) + '.' + extension
        if os.path.exists(file_name):
            file_name = os.path.join(path, random_name(min_len, max_len) + str(i)) + '.' + extension
        with open(f'{path}/{file_name}_{i}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


def path_exist(path):
    if not os.path.exists(path):
        Path(path).mkdir()


create_file('txt', file_count=10)
