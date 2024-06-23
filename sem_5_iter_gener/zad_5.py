# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

for i in range(1, 101):
    if not i % 3 and not i % 5:
        print("FizzBuzz", end=' ')
    elif not i % 5:           # тоже самое i % 3 == 0
        print("Buzz", end=' ')
    elif i % 3 == 0:
        print("Fizz", end=' ')
    else:
        print(i, end=' ')
print()

fizz_buzz = ('FizzBuzz' if not i % 3 and not i % 5 else ('Fizz' if not i % 3 else ('Buzz' if not i % 5 else i)) for i in
range(1, 101))  # однострочник

print(*fizz_buzz)