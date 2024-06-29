"""
Задача для самостоятельного решения
1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
"""


def get_even_num(lst1):
    res_lst = []
    for elem in lst1:
        if elem % 2 == 0:
            res_lst.append(elem)
    return res_lst


def get_square_num(lst):
    res2_lst = []
    for el in lst:
        tmp_lst = []
        tmp_lst.append(el)
        tmp_lst.append(el ** 2)
        tpl = tuple(tmp_lst)
        res2_lst.append(tpl)
    return print('Итоговый результат: \n', res2_lst)


str1 = '1 2 3 5 8 15 23 38'
print('Исходная строка:', str1)
lst1 = map(int, str1.split())
get_square_num(get_even_num(lst1))

# Более кратко
str2 = '1 2 3 5 8 15 23 38'
print()
print('=' * 50)
print('Исходная строка:', str2)
lst2 = map(int, str2.split())
res = list()
for elm in lst2:
    if elm % 2 == 0:
        res.append((elm, elm ** 2))
print('Итоговый результат: \n', res)
print('=' * 50)

# Через lambda, filter, map

str3 = '1 2 3 5 8 15 23 38'
print()
print('=' * 50)
print('Исходная строка:', str3)
map1 = map(int, str3.split())  # объект map, не список
filter1 = filter(lambda x: x % 2 == 0, map1)  # объект filter, не список
lst5 = list((map(lambda x: (x, x ** 2), filter1)))  # а вот это уже список, т.к. есть list
print(lst5)
