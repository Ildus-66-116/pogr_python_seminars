# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

TWO = 2
EIGHT = 8

result = ''
num = int(input('Type num: '))
print(bin(num))
if num == 0:
    result = '0'
while num != 0:
    result = str(num % TWO) + result
    num = num // TWO
else:
     result = '0b' + result
print(result)

print(oct(num))

while num != 0:
    result += str(num % EIGHT)
    num = num // EIGHT
else:
    result = '0o' + result
print(result[::-1])


