# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

rows = int(input("Количество рядов: "))
space = rows - 1
for i in range(rows):
    print(' ' * (space - i) + '*' * (1 + i * 2))
