"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

import os

flag = True
while flag:
    month = int(input('Введите номер месяца в году: '))
    if month > 0 and month <= 12:
        flag = False
    else:
        print('Некорректный номер месяца! Попытайтесь еще раз!')
        os.system('pause')

seasons = ['зима', 'весна', 'лето', 'осень']
if month == 1 or month == 2 or month == 12:
    print(seasons[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])
else:
    print(seasons[3])

print('--------------via dict-----------------\n')
dict_season = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
               10: 'осень', 11: 'осень', 12: 'зима'}
for key in dict_season:  # перебор ключей словаря
    if month == key:  # сравнение и вывод значения
        print(dict_season[key])
