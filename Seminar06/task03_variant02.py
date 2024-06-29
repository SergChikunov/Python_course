"""
Задача №45. Общее обсуждение
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:
300

Вывод: 220 284

Решение рекурсивными функциями, представленное на семинарском занятии
"""

from sys import setrecursionlimit  # импорт модуля определения глубины рекурсии

k = int(input('k = '))  # получаем k  с консоли, это значение до которого ведем поиск дружественных чисел
setrecursionlimit(10 ** 5)  # глубина рекурсии, необходима чтобы избежать переполнения стека значений


def pairs(array):  # функция определения пар дружественных чисел
    if len(array) == 0:  # если длина списка равна 0, то
        return  # просто выходим из функции не возвращая ничего
    # Далее, извлекаем из списка первый элемент. Это нужно для того, чтобы сработало условие
    # в базовом случае
    pairless = array.pop(0)
    # Помним, каждый элемент списка - кортеж, в  котором два значения: первое - элемент, второе - сумма его делителей.
    # Это важно для понимания цикла, объявленного далее
    for i in array:
        if i[0] == pairless[1] and i[1] == pairless[0]:  # сравниваем элементы соседних кортежей, при выполнении условия
            print(f'{pairless[0]} {i[0]}')  # выводим пары дружественных чисел
    return pairs(array)  # рекурсивный вызов


def denominators(n, s=1, all_numbers_denominators=None):  # функция поиска делителей числа, где: n - конечное значение,
    # s - начальное значение, all_numbers_denominators - список делителей числа
    if all_numbers_denominators is None:  # если список имеет значение None, то
        all_numbers_denominators = []  # обращаем его в пустой список
    if s > n:  # базовый случай, если значение s больше n, возвращаем all_numbers_denominators
        return all_numbers_denominators
    denominator_sum = 0  # приравниваем сумму делителей для текущего числа к 0
    """
    Наибольшим делителем у любого числа является само это число. 
    Вторым по старшинству делителем будет половина нашего исходного числа. 
    Значит мы можем искать делители в цикле на интервале от 1 до n // 2.
    Прибавляем 1, т.к. значение верхней границы range() не попадает в обработку по умолчанию
    """
    for i in range(1, s // 2 + 1):
        if s % i == 0:  # если число делится нацело на i, то
            denominator_sum += i  # добавляем его к сумме делителей
    all_numbers_denominators.append(
        (s, denominator_sum,))  # добавляем в список кортеж, первое значение которого число,
    # второе - сумма его делителей
    return denominators(k, s + 1, all_numbers_denominators)  # рекурсивный вызов, увеличиваем только начальное значение


pairs(denominators(k))
