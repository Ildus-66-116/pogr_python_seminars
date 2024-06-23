# Задание №1
# � Вспомните какие модули вы уже проходили на курсе.
# � Создайте файл, в котором вы импортируете встроенные в
# модуль функции под псевдонимами. (3-7 строк импорта).

from random import randint as rdi, uniform as uni
from sys import builtin_module_names as bmn
print(rdi(1, 10))
print(uni(1,10))