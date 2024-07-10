import pandas as pd
import numpy as np

start_date = '20210101'
ave_data = np.array(np.arange(40)).reshape((10, 4))  # numpy массив 6х4
dates = pd.date_range(start_date, periods=10)  # даты на полгода
# создание DataFrame из ave_data, в качестве индекса берем dates, в качестве полей значения списка columns
ave_df = pd.DataFrame(ave_data, index=dates, columns=list('ABCD'))
print(ave_df)
print('=' * 50)
print()
# добавим столбец в наш датафрейм, имя столбца - 'Cars'
ave_df_cars = ave_df.copy()
ave_df_cars['Cars'] = ['Ford', 'Opel', 'Mazda', 'Mitsubishi', 'Renault', 'Lada', 'Hammer', 'BMW', 'Mercedes', 'VW']
print(ave_df_cars)
print('=' * 50)
print()
# обращение к индексам строки
print(pd.date_range(start_date, periods=10))
print('=' * 50)
print()
# Panda Series как структура данных, рассматривается как одномерный массив
print(pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=pd.date_range(start_date, periods=10)))
print('=' * 50)
print()
# добавим сформированный pd.Series к датафрейму, в качестве отдельного поля, а в качестве дополнения умножим значения
# на 10 и приплюсуем 5, подобные действия могут пригодиться на практике для подведения различных итогов
ave_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=pd.date_range(start_date, periods=10))
ave_df['Extra'] = ave_series * 10 + 5
print(ave_df)
print('=' * 50)
print()

# добавим pd.Series к датафрейму ave_pf_cars, в качестве отдельного поля
ave_df_cars['Extra'] = ave_series * 10 + 5
print(ave_df_cars)
print('=' * 50)
print()
# заменим значение элемента в поле Cars Renault на Citroen, выполняется данное действие таким образом, где at -
# индекс-оператор
ave_df_cars.at[dates[4], 'Cars'] = 'Citroen'
print(ave_df_cars)
print('=' * 50)
print()
# еще один индекс-оператор - iat, где: первый индекс - строка, второй - поле
ave_df_cars.iat[3, 2] = 678
print(ave_df_cars)
print('=' * 50)
print()
# взаимодействие Pandas и numpy, создадим при помощи numpy массив, затем передадим ему датафрейм ave_df_cars
# произведем с ним арифметические действия и отобразим результат
print(len(ave_df_cars))
ave_new_array = np.array(np.arange(len(ave_df_cars))) * 10 + 5
print(ave_new_array)
print('=' * 50)
print()
# добавим полученный массив в качестве нового поля в датафрейм ave_df_cars
ave_df_cars['E'] = ave_new_array
print(ave_df_cars)
print('=' * 50)
print()
