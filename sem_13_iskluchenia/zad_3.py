"""Создайте класс с базовым исключением и дочерние классы исключения:
ошибка уровня,
ошибка доступа."""

class MyException(Exception):
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return f'{self.message}'


class LevelError(MyException):
    def __init__(self, msg: str):
        super().__init__(msg)


class PassException(MyException):
    pass
