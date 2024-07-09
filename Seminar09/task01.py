"""
Задача №1. Решение в группах
1. Прочесть с помощью pandas файл california_housing_test.csv
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv

filename = 'california_housing_test.csv'
data = read_csv(filename)
print(data)  # вывод датафрэйма
print('=' * 50)
print(data.shape)  # вывод краткой информации о полях и записях датафрэйма
print('=' * 50)
print(data.dtypes)  # тип данных какждого поля датафрэйма
print('=' * 50)
print(data.info())  # информация о каждом поле датафрэйма
print('=' * 50)
print(data.describe())  # аналитика по каждому полю датафрэйма
