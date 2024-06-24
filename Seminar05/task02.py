"""
Вывести последовательность Фибоначчи до позиции указанной с консоли
"""

def fibon_num(n):
    if n in [1, 2]:
        return 1
    return fibon_num(n - 1) + fibon_num(n - 2)


list_1 = []
number = int(input('Введите целое, неотрицательное число: '))
for i in range(1, number):
    list_1.append(fibon_num(i))
print(list_1)