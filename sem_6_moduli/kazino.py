from random import randint as rdi


def number_generator(start, stop, number):
    count = 0
    hidden_number = rdi(start, stop)
    while count < number:
        user_number = int(input('Введите число: '))
        count += 1
        if user_number < hidden_number:
            print("Загаданое число больше")
        elif user_number > hidden_number:
            print("Загаданое число меньше")
        else:
            print(f'Поздравляю вы угадали! {hidden_number}')
            return True
    print(f'Не угадали, загаданное число {hidden_number}')
    return False
