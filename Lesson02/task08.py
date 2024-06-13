"""

Лекция 2. Множества. Знакомиство
Множества содержат в себе уникальные(!!!) элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. Если есть два множества, можно совершать над ними
любые стандартные операции, например, объединение, пересечение и разность.
"""

# my_set = set()  # создание пустого множества
# print(type(my_set))  # проверка типа объекта
colors = {'red', 'green', 'blue'}  # множество, ЗАПОМНИТЬ - уникальные элементы, их порядок не важен!!!
print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')  # пробуем добавить во множество существующий элемент
# print(colors)  # {'red', 'green', 'blue'} - вот что получим на выводе, ошибок не будет, тоже это учесть на будущее!
colors.add('gray')  # добавление элемента во множество, при этом новый элемент попадает на случайную позицию!
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')  # удаление элемента из множества
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' - Oooops! При попытке удалить несуществующий элемент множества получим ошибку!
colors.discard('red')  # discard  - проверит начличие элемента во множестве, если он есть - удалит, если его нет, то ошибки не будет и код продолжит выполнение!
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { } - очистка множества - удаление всех его элементов
print(colors)  # вывод - пустое множество
