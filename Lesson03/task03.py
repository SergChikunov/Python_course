"""
Возможность передачи неограниченного количества аргументов в функцию
● Можно указать любое количество значений аргумента функции.
● Перед аргументом надо поставить *.
В примере ниже функция работает со строкой, поэтому при введении чисел программа выдаёт ошибку
"""


def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res


print(concatenatio('H', 'e', 'l', 'l', 'o', ',', ' ', 'a', 'l', 'l', '!'))
