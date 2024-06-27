"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""

num_1 = [3, 1, 3, 4, 2, 4, 12]
num_2 = [4, 15, 43, 1, 15, 1]
num_3 = []

for el in num_1:
    if el not in num_2:
        num_3.append(el)
print('Решение циклом for')
print(num_3)

num_4 = list(elem for elem in num_1 if elem not in num_2)
print('\nРешение с применением List comprehension')
print(num_4)

res = filter(lambda elem: elem not in num_2, num_1)
print('\nРешение через использование функций filter и lambda')
print(', '.join(str(elem) for elem in res))