"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел A. Последняя строка содержит число X
"""

list_len = int(input('Введите длину массива: '))
my_list = []
i = 0
while i < list_len:
    next_el_list = int(input(f"Введите {i} элемент массива, не меньше 1: "))
    my_list.append(next_el_list)
    i += 1
x_value = int(input('Введите искомое число: '))
print('Итоговый список элементов: \n', my_list)
num_count = my_list.count(x_value)
print(f"Значение {x_value} встречается в списке {num_count} раз(а)" if num_count > 0 else 'Нет такого элемента в списке')
