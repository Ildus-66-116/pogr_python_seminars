"""Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например, отлавливаем ошибку деления на ноль.
"""
import logging

FORMAT = ('{levelname:<8} - {asctime}. В модуле "{name}" '
          'в строке {lineno:03d} функция "{funcName}()" '
          'в {created} секунд записала сообщение: {msg}')

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log.txt', filemode='w', encoding='utf-8', level=logging.WARNING,
                    format=FORMAT, style='{')


def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError as e:
        logger.error(msg=e)


if __name__ == '__main__':
    print(division(4, 2))
    print(division(4, 0))
