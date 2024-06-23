"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def division_nums(num_1, num_2):
    try:
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0?!!!')


first_num = int(input('Введите делимое: '))
second_num = int(input('Введите делитель: '))
print('Результат деления =', division_nums(first_num, second_num))