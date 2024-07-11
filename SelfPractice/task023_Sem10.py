"""
Задача №2. Решение в группах
Написать EDA для датасета про пингвинов
Необходимо:
- Использовать 2-3 точечных графика
- Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
- Использовать PairGrid с типом графика на ваш выбор
- Изобразить Heatmap
- Использовать 2-3 гистограммы
"""
# import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl

penguins = sns.load_dataset("penguins")
print(penguins.head())
print(penguins.info())
sns.scatterplot(data=penguins, x="sex", y="body_mass_g")  # first subtask

# second subtask
# sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", size='bill_length_mm', hue='bill_length_mm',
#                 sizes=(10, 100))
# sns.scatterplot(data=penguins, x="body_mass_g", y="bill_length_mm", hue='island', style='species')  # second chart

# third subtask
# поля входящие в график
"""
data_columns = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
graph = sns.PairGrid(penguins[data_columns], hue='body_mass_g', palette='deep')  # определение опций графика
graph = graph.map_diag(mpl.hist)  # графики по диагонали
graph = graph.map_offdiag(mpl.scatter)  # типы остальных графиков
body_mass = {'light': 3000, 'light_heavy': 4000, 'medium': 5000, 'medium_heavy': 5500, 'heavy': 6000}
graph = graph.add_legend(legend_data=body_mass, title='Масса тушки')  # добавить данные легенды
"""

# forth subtask
# sns.displot(data=penguins, x='flipper_length_mm', y='body_mass_g', cbar=True)

# fifth subtask
# sns.displot(data=penguins, x='body_mass_g', kind='hist', col='sex', hue='species')

mpl.show()
