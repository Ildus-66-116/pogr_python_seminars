# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

from sys import argv
from kazino import number_generator

start, stop, number = 1, 100, 10
argv = list(map(int, argv[1:]))
if len(argv) >= 1:
    start = argv[0]
if len(argv) >= 2:
    stop = argv[1]
if len(argv) >= 3:
    number = argv[2]

number_generator(start, stop, number)

