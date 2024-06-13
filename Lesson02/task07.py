"""

Лекция 2. Словари. Работа со словарем
"""

#  dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary)  # {'up': '↑', 'left': '⇐', 'down': '↓', 'right': '→'}
# print(dictionary['type']) # KeyError: 'type' - нет такого ключа в словаре
# del dictionary['left'] # удаление элемента, причем удаление ключа означает утрату его значения, но не наоборот!!!
for item in dictionary:  # вывод словаря
    print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →
print()
for (k,v) in dictionary.items():  # другой вариант вывода словаря, где k - ключ, v - значение
    print(k, v)
print()
# пояснить нужно упоминание dictionary.items() - это обращение к элементам словаря в формате ключ: значение
print(dictionary.items())  # вывод: dict_items([('up', '↑'), ('left', '⇐'), ('down', '↓'), ('right', '→')])
"""
В предыдущем примере представлен вывод при обращении ко всем элементам словаря
На выводе мы получаем список (list), элементами которого являются кортежи (tuple), каждый из которых содержит 
пару значений словаря в виде ключ:значение 
"""
