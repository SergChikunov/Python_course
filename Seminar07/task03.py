"""
Задача №3. Решение в группах
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его
характеристику.
Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)

Вывод: same
"""


def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))  # из результата вызова функции lambda
    #  делаем множество, set - набор элементов без дубликатов
    # таким образом, если длина множества =1,
    # то элементы в заданном списке имеют одинаковые характеристики
    # если длина множества =0, значит заданный список был пустым
    # в этом случае по условию, мы также должны вернуть True
    return True if len(my_set) == 1 or len(my_set) == 0 else False


def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2  # т.к. имеется оператор сравнения, то вернется тип bool


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
