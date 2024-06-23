"""Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    __slots__ = '_side_a', '_side_b'  # экономия памяти и защита

    def __init__(self, side_a, side_b=None):
        self._side_a = side_a
        self._side_b = side_a if side_b is None else side_b

    @property
    def side_a(self):
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self._side_a = value
        else:
            raise ValueError()

    @side_a.getter
    def side_a(self):
        return self._side_a * 10


if __name__ == '__main__':
    rectangle = Rectangle(5, 4)
    print(rectangle.side_a)
    rectangle.side_a = 6
    print(rectangle.side_a)
    print(rectangle.__slots__)
