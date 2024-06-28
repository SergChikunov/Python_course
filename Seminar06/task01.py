"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""

num_1 = [3, 1, 3, 4, 2, 4, 12]
num_2 = [4, 15, 43, 1, 15, 1]
num_3 = []
# num_5 = list(map(int, input('Введите числа через пробел...').split()))


# for el in num_1:
#     if el not in num_2:
#         num_3.append(el)
# print('Решение через традиционный итератор с функцией append')
# print(num_3)


def func(num1, num2, num3=[]):
    if len(num1) == 0:
        return num3
    if num1[0] not in num2:
        num3.append(num1[0])
    return func(num1[1:], num2, num3)


print(func(num_1, num_2, num_3))

# num_4 = [elem for elem in num_1 if elem not in num_2]
# print('\nРешение с применением List comprehension')
# print(num_4)
#
# res = filter(lambda elem: elem not in num_2, num_1)
# print('\nРешение через использование функций filter и lambda')
# print(', '.join(str(elem) for elem in res))
