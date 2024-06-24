"""
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

number = "3 4"


def func1(data):
    new_data = ""
    for s in reversed(data):
        new_data += s
    return new_data


print(func1(number))


def func2(data, new_data=""):
    if len(data) == 0:
        return new_data
    return func2(data[:-1], new_data+data[-1])


print(func2(number))
