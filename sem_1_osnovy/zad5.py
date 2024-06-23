# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n

n = int(input('введите n:'))
e = int(input('введите e:'))
count = 0
result = 0
while count < n:
    if count % 2 == 0 and count % e != 0:
        result += count
    count += 1
print('Summa:', result)
