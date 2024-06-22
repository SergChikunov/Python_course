"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

"""

import random

num_1 = int(input('Укажите количество элементов первого списка: '))
num_2 = int(input('Укажите количество элементов второго списка: '))
list_1 = [random.randint(0, 50) for i in range(num_1)]  # использование comprehension list для первого списка
list_2 = [random.randint(0, 50) for j in range(num_2)]  # использование comprehension list для второго списка
print('\nПервый список такой:')
print(list_1)
print('\nВторой список такой:')
print(list_2)
print()
set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set_2.intersection(set_1)
print('set_3 =', set_3)
list_res = list(set_3)
list_res.sort()
if len(list_res) == 0:
    print('В заданных списках нет повторяющихся значений!')
else:
    print('В обеих списках присутствуют такие значения: ')
    print(*list_res)