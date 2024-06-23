# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def is_profit(dict_company: dict) -> bool:
    # for  items in dict_company.values():
    #     if sum(items)< 0:
    #         return False
    # return True
    # return all([sum(value) > 0 for value in dict_company.values()])
    return all(map(lambda x: sum(x) > 0, dict_company.values()))


companies = {
    'Abibas': [1234, -456, 2345, 1000, 800],
    'Nuke': [-3000, 5600, -8000],
    'Ribok': [5000, -2300, -4000, 9000]
}

print(is_profit(companies))
