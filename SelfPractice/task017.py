"""
Дома расположены в определенной "полосе" долготы и широты. Изображение точек долготы по отношению к широте
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl


df = pd.read_csv('california_housing_train.csv')
# print(df.info())
print(df.head())

# sns.scatterplot(data=df, x="longitude", y="latitude")
# sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")
# sns.scatterplot(data=df, x="households", y="population", size="total_rooms")
# mpl.show()

# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sns.PairGrid(df[cols])  # использование метода PairGrid() дает возможность построения зависимых отношений
# g.map(sns.scatterplot)  # строим зависимости
# mpl.show()
