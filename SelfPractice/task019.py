import pandas as pd
import numpy as np

ave_data = np.array(np.arange(24)).reshape((6, 4))  # numpy массив 6х4
dates = pd.date_range('20210101', periods=6)  # даты на полгода

# создание DataFrame из ave_data, в качестве индекса берем dates, в качестве полей значения списка columns
ave_df = pd.DataFrame(ave_data, index=dates, columns=list('1234'))
print(ave_df)
print('=' * 50)
print()
# простой вывод колонки с наименованием '4', не забывай про индексы(!!!), это индекс 3
print(ave_df['4'])
print('=' * 50)
print()
# демонстрация срезов, и в данном случае выводятся уже строки !!!
print(ave_df[1:4])
print('=' * 50)
print()
# еще срез по строкам, но в качестве диапазона указаны наименования строк (даты)
print(ave_df['2021-01-02':'2021-01-05'])
print('=' * 50)
print()
# использование атрибута loc (от location) для вывода того же диапазона
print(ave_df.loc[dates[1:5]])
print('=' * 50)
print()
# вывод всех строк, но из столбцов берем только '1' и '2'
print(ave_df.loc[:, ['1', '3']])
print('=' * 50)
print()
# срез по строкам, но из столбцов берем только '1' и '2'
print(ave_df.loc['2021-01-02':'2021-01-05', ['1', '3']])
print('=' * 50)
print()
# со значениями датафрейма можно проводить арифметические операции, например, из строки 2010-01-02 возьмем значение с
# индексом [1], и умножим это значение на 5
# также было получено предупреждение:
# In a future version, integer keys will always be treated as labels (consistent with DataFrame behav):
# В будущей версии целочисленные ключи всегда будут рассматриваться как метки (в соответствии с поведением DataFrame).
# print(ave_df.loc['2021-01-02', ['1', '3']][1] * 5)
# print('=' * 50)
# print()
# обращение к отдельно взятому элементу, переменная dates хранит индексы значений элементов, используем ее для
# получения значения требуемого элемента
print(ave_df.loc[dates[1], '1'])
print('=' * 50)
print()
# ave_data - это массив, объявленный в самом начале, поэтому можно обращаться к элементам как это принято в Python
print(ave_data[2])
print('=' * 50)
print()
# тот же результат можно получить использовав функцию iloc() (от integer location) обратившись к датафрейму
print(ave_df.iloc[2])
print('=' * 50)
print()
# iloc() также работает со срезами, до запятой срез по строкам, после - по полям
print(ave_df.iloc[1:3, 1:5])
print('=' * 50)
print()
# а можно просто перечислить строки и столбцы через запятую
print(ave_df.iloc[[0, 3], [1, 2, 3]])
print('=' * 50)
print()
# можно указывать операторы сравнения для выборки данных, в данном случае нам будут показаны все элементы датафрейма
# значения которых > 5, остальные значения будут помечены как NaN (Not any Number), рассматривать такое значение в
# свете программного кода необходимо как пустое значение
print(ave_df[ave_df > 5])
print('=' * 50)
print()

