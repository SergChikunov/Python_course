"""
Задача: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1
столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)  # перемешивание значений списка в случайном порядке
data = pd.DataFrame({'whoAmI': lst})  # формирование DataFrame
print(data.head(20))  # показываем DataFrame, чтобы знать с чем работаем
print('=' * 50)
print()
print(pd.get_dummies(data['whoAmI']))  # результат функции get_dummies, требуется получить аналогичный, без ее использ.
print('=' * 50)
print()

data_one_hot = data.copy()  # делаем копию исходного датафрейма в data_one_hot
# если значение поля whoAmI = human, то в столбец human добавляем значение True
data_one_hot.loc[data_one_hot['whoAmI'] == 'human', ['human']] = True
# если значение поля whoAmI = robot, то в столбец robot добавляем значение True
data_one_hot.loc[data_one_hot['whoAmI'] == 'robot', ['robot']] = True
data_one_hot = data_one_hot.fillna(value=False)  # все поля с NaN заполняем значением False
data_one_hot.drop(data_one_hot.columns[[0]], axis=1, inplace=True)  # удаляем первый столбец в итоговом DataFrame

print(data_one_hot.head(20))  # выводим результат, результат совпал с выводом get_dummies() - задача решена
