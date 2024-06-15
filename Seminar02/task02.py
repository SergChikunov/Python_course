"""

Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""


a = 5
fibo_p, fibo_n = 0, 1  # первые два числа последовательности
position = 2  # есть первые два числа последовательности, соответсвенно мы на 2 месте последовательности
while fibo_n < a:
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n  # определяем последующие члены последовательности
    position += 1
if fibo_n == a:  # определяем что же получилось по итогу решения задачи
    print(position)
else:
    print(-1)


def func(a=5, fibo_p=0, fibo_n=1, position=2):  # рекурсия
    if fibo_n == a:  # базовый случай
        return position
    elif fibo_n < a:
        return func(a, fibo_n, fibo_p + fibo_n, position + 1) # рекурсивный вызов
    else:
        return -1


print(func())