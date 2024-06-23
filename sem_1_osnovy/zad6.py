# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


# MAIN_CON = 4
# ADD_CON = 100
# ISKL_CON = 400
#
# year = int(input("Введите год yyyy: "))
# if (year % MAIN_CON != 0 or year % ADD_CON == 0
#         and year % ISKL_CON != 0):  # ленивый if если в 1 части false далее and не проверяется
#     print(f'{year} - обычный')
# else:
#     print(f'{year} - високосный')


FOUR = 4
FOUR_HUNDRED = 400
HUNDRED = 100
GRIG_CAL = 1582
year = int(input("Please write year: "))
leap = False

if year >= GRIG_CAL:
    if year % FOUR_HUNDRED == 0:
        leap = True
    elif year % FOUR == 0:
        if year % HUNDRED != 0:
            leap = True
print("Is year {} a leap year? {}".format(year, leap) if leap else "Year is not valid for task")