# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def text_list(text: str):
    # result = []
    # for i in set(text):
    #     result.append(ord(i))
    # return sorted(result, reverse=True)
    return sorted([ord(i) for i in set(text)], reverse=True)    # то же самое что выше


input_text = input('Введите текст: ')
print(text_list(input_text))
