import pandas as pd
import numpy as np

laptops = ['Lenovo', 'Dell', 'HP', 'Chromebook', 'MacBook']

laptops_df = pd.DataFrame({
    'price': [350, 400, 500, 560, 1000],
    'disk_space': [0.5, 1, 2, 3, 1.5]},
    index=laptops)
print(laptops_df)
print('=' * 50)
print()

# предположим, что Chromebook заменили на Huawei и мы должны поправить этот момент в нашем датафрейме
# создадим новый датафрейм, реиндексируем его содержимое с учетом изложенного выше и посмотрим на результат
more_laptops = ['Lenovo', 'Dell', 'HP', 'Huawei', 'MacBook']
laptops_df_2 = laptops_df.reindex(more_laptops)
print(laptops_df_2)  # в результате мы увидим, что значения стоимости и объема диска стали NaN значениями
print('=' * 50)
print()
# воспользуемся возможностями Pandas и удалим из датафрейма все значения NaN, для этого используем dropna()
laptops_df_3 = laptops_df_2.dropna(how='any')
print(laptops_df_3)  # как можно увидеть по результату, строка Huawei полностью была удалена
print('=' * 50)
print()
# можно пойти другим путем - заполнить отсутствующие значения, для этого используем fillna()
laptops_df_3 = laptops_df_2.fillna(value=100)
print(laptops_df_3)  # указанное значение попадет во все ячейки датафрейма со значениями NaN
print('=' * 50)
print()
# можно также проверить датафрейм на отсутствующею значения функцией isnull(), функция проставит булево значение
# в ячейках датафрейма
print(laptops_df_2.isnull())  # там где находились NaN значения, мы увидим True
print('=' * 50)
print()
# есть возможность подсчета нулевых значений в датафрейме
print(laptops_df_2.isnull().sum())
print('=' * 50)
print()
# можно устанавливать опции для отображения значений элементов, например, установим для всех элементов вывод с двумя
# значениями после замятой
pd.set_option('display.precision', 2)  # учитываем, что устанавливаем опцию для всего дальнейшего использования Pandas
print(laptops_df_2.describe())
print('=' * 50)
print()
# использование функции получения среднего значения по всему датафрейму
print(laptops_df_2.mean())
print('=' * 50)
print()
# использование функции получения среднего значения по первой строке датафрейма
print(laptops_df_2.mean(1))
print('=' * 50)
print()
# при помощи функции apply() можно применять различные функции уже к набору элементов, например кумулятивная сумма
# из numpy на первом столбце
print(laptops_df_2.apply(np.cumsum, axis=0))
print('=' * 50)
print()
