# 1 Удаление пустых строк
name = ['Hello', "", 'World', ""]
new_name = []
for i in name:
    if i != "":
        new_name.append(i)
print(new_name)

# 2 Список в квадрате
name1 = [i ** 2 for i in range(5)]
print(name1)

# 3 Удаление вхождений числа 20
name3 = [5, 10, 15, 20, 25, 50, 20]
print(list(filter(lambda x: name3.count(x) == 1, name3)))

# 4 Список в обратном порядке
name4 = [123, 345, 542, 65462]
print(name4.reverse())
print(name4)

# 5 Поменял местами большее с меньшим числом
name5 = [1, 2, 3, 4, 5]
name5[0], name5[4] = name5[4], name5[0]
print(name5)

# 6 Вывести повторяющейся элемент
name6 = [12, 32, 12, 45, 12]
print(*filter(lambda x : name6.count(x) > 1, name6))

# 7 Сумма списка
name7 = [21, 32, 12]
print(sum(name7))
