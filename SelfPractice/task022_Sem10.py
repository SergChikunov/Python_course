"""
Задача №1. Решение в группах
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношению к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl

df = pd.read_csv('california_housing_train.csv')
# print(df.info())
# print(df.head())

# sns.scatterplot(data=df, x="households", y="population")  # 1 subtask
# sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)  # 2 subtask
# sns.histplot(data=df, x="housing_median_age")  # 3 subtask

# 4 subtask
# Значения в housing_median_age от 1 до 52 с шагом 1, это чересчур много для отображения в легенде
# Создадим отдельный список для legend_mark с шагом кратным пяти
my_list_marks = []
for i in range(1, 60, 4):
    my_list_marks.append(i)

my_plot = sns.histplot(data=df, x="median_house_value", hue='housing_median_age')  # 4 subtask
# определяем название легенды, размещение, прикручиваем тень к ней, проставляем метки данных
mpl.legend(title="housing_median_age", loc='best', bbox_to_anchor=(1, 1), shadow=True, labels=my_list_marks)
mpl.show()
