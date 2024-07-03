import pandas as pd

df = pd.read_csv('employees.csv')  # чтение csv в Pandas DataFrame

print(df)  # печать Pandas DataFrame


print('\nПример доступа к столбцу name')
names = df['name']  # доступ к столбцу name
print(names)
