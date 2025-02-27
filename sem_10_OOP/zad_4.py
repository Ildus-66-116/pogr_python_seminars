"""Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from zad_3 import Person


class Worker(Person):
    def __init__(self, name, surname, age, id: int):
        super().__init__(name, surname, age)
        self.id = id
        self.access_level = sum(map(int, str(id))) % 7

    def worker_info(self):
        return f'{self.full_name()} and my id is {self.id} and my access level {self.access_level}'


if __name__ == '__main__':
    worker = Worker('Dima', 'Frolov', 42, 100001)
    print(worker.worker_info())
