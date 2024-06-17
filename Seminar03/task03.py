"""
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
           {" VIII ": " S007 "}]
print('Исходный словарь: \n', my_list)
print(type(my_list[0]))  # тип элемента списка
my_set = set()  # пустое множество
for i in range(len(my_list)):  # цикл для элементов списка - число
    for value in my_list[i].values():  # в этом цикле получаем значение элемента словаря, не ключ!!!
        print('dict_value =', value)  # проверка, что получаем значение словаря
        my_set.add(value.strip())  # добавляем элемент словаря во множество, попутно удалив начальный и конечный пробел
print('Уникальные значения из словарей в исходном списке: \n', my_set)  # выводим итог решения