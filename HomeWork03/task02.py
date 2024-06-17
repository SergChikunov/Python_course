"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел A. Последняя строка содержит число X

5
1 2 3 4 5
6
-> 5
"""

list_len = int(input('Введите длину списка: '))
my_list = []
i = 0
while i < list_len:
    next_el_list = int(input(f"Введите {i} элемент списка, не меньше 1: "))
    my_list.append(next_el_list)
    i += 1
x_value = int(input('Введите число для сравнения: '))
if x_value in my_list:
    print('Ближайший элемент списка: ', x_value)
else:
    my_list.sort()
    print('Заданный список: ', my_list)
    if len(my_list) == 1:
        print('Ближайший элемент списка: ', my_list[0])
    i = len(my_list) - 1
    while i >= 0:
        if x_value > my_list[i]:
            print('Ближайший элемент списка: ', my_list[i])
            break
        i -= 1
