"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра"""

"""Добавьте к задачам 1 и 2 строки документации для классов."""


class MyClass:
    """Мой класс добавляет свойства класса"""
    _my_list = []

    def __init__(self, number, mystr):
        self.number = number
        self.mystr = mystr

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.archiv = MyClass._my_list.copy()
        MyClass._my_list.append(instance)
        return instance

    def __repr__(self):
        return f'MyClass({self.number}, {self.mystr})'


if __name__ == '__main__':
    cl_1 = MyClass('1', 'Hello')
    cl_2 = MyClass('2', 'Привет')
    cl_3 = MyClass('3', 'Hi')

    print(cl_1.archiv)
    print(cl_2.archiv)
    print(cl_3.archiv)
