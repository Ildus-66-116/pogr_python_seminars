# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

sample_list = [1, 2, 1, 1, 2, 5, 6, 5, 5, 6, 7]

for item in set(sample_list):
    if sample_list.count(item) == 2:
        sample_list.remove(item)
        sample_list.remove(item)
print(sample_list)
