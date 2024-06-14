"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

str_val = '1 2 3'  # исходная строка
str_list = str_val.split()  # преобразуем строку в список
print('Исходный список:', str_list)
dl = len(str_list)  # в переменную заносим длину списка
for i in range(0, dl, 2):  # обрабатываем список с шагом 2
    temp = str_list.pop(i)  # извлекаем i-ый элемент и запоминаем его в переменной
    str_list.insert(i + 1, temp)  # вставляем извлеченный элемент на одну позицию старше
print('Модифицированный список:', str_list)
