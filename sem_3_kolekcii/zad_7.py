# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = input("Введите текст: ")

dict_text = dict()

for char in text:
    # if char in dict_text:
    #     dict_text[char] += 1
    # else:
    #     dict_text[char] = 1
    dict_text[char] = dict_text.get(char, 0) + 1

print(dict_text)

text = input("Введите текст: ")

dict_text = dict()

for char in set(text):
    dict_text[char] = text.count(char)
print(dict_text)