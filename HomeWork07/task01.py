"""
Задача 2: Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве
аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Ввод:
print_operation_table(lambda x, y: x * y, 6, 6)

Вывод:
1   2   3   4   5   6
2   4   6   8   10  12
3   6   9   12  15  18
4   8   12  16  20  24
5   10  15  20  25  30
6   12  18  24  30  36

"""


def print_operation_table(operation, x=9, y=9):
    if x < 2:
        return print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    for j in range(1, x + 1):
        for i in range(1, y + 1):
            if i < y:
                print(operation(j, i), end=' ')
            else:
                print(operation(j, i))


print_operation_table(lambda x, y: x * y, 5, 7)
