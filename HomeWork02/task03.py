"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Пример
n=16

#Вывод
1
2
4
8
16
"""

n = int(input('Введите целое неотрицательное число: '))

res = 0
i = 0
while i < n - 1:  # пожалуй, самое эффективное решение, с точки зрения затрат ресурсов и получаемого результата
    res = 2 ** i
    if res <= n:
        print(res)
    i += 1

print('-----for01-----')  # результат верный, но код продолжает работать, после достижения результата, что не эффективно
res = 0
for j in range(n):
    res = 2 ** j
    if res <= n:
        print(res)

print(
    '-----for02-----')  # здесь код работает до достижения результата, но использован break, что считаетсч плохим стилем написания кода
res = 0
for j in range(n):  # код выдает лишнюю позицию
    res = 2 ** j
    print(res)
    if res >= n:
        break