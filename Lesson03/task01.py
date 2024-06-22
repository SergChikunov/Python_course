"""
Задание 1. Посчитать сумму чисел от 1 до введенного пользователем.
Оформить задание в виде функции
"""

def sum_numbers(n):  # объявление функции, в скобках параметры

    summa = 0
    for i in range(1, n + 1):  # n + 1 потому что должно быть включено в диапазон вычислений
        summa += i
    return summa


n = int(input('Введите число: '))  # 5
print(sum_numbers(n))  # 15; вызов функции и передача аргумента
