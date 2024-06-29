"""
Функция filter, метод split()
Задана строка, состоящая из чисел, необходимо вывести из нее значения, которые кратны 5
"""

str1 = '15, 65, 9, 36, 175'
print('Исходная строка: ', str1)
list_1 = list(map(int, str1.split(', ')))
lst_res = list(filter(lambda el: el % 5 == 0, list_1))
print()
print('Значения которые кратны 5:', *lst_res)
