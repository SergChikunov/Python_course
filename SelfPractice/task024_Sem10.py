"""
Задача №3. Решение в группах
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""
# import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl

penguins = sns.load_dataset("penguins")
print(penguins.info())

# формируем условие из задания: если длина клюва менее 33, то вносим в добавляемый столбец bill_length_mark
# значение low (хотя, IMHO, правильней было бы вносить: short, middle, long), и так далее по условию, делим на 3 группы
penguins.loc[penguins['bill_length_mm'] < 33, 'bill_length_mark'] = 'low'
penguins.loc[
    (penguins['bill_length_mm'] >= 33) & (penguins['bill_length_mm'] < 42), 'bill_length_mark'] = 'middle'
penguins.loc[penguins['bill_length_mm'] >= 42, 'bill_length_mark'] = 'high'

print(penguins.head(15))  # проверяем добавился ли столбец в датафрейм, а также его значения
print(penguins.tail(15))

# для наглядности отобразим на графике внесенный столбец относительно пола и породы тушки
sns.displot(data=penguins, x='bill_length_mark', kind='hist', col='sex', hue='species')
mpl.show()
