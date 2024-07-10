"""
Когда дело доходит до выбора строк и столбцов кадра данных pandas, loc и iloc — это две часто используемые функции.
Вот тонкая разница между двумя функциями:
loc выбирает строки и столбцы с определенными метками
iloc выбирает строки и столбцы в определенных целочисленных позициях
В следующих примерах показано, как использовать каждую функцию на практике.
"""
import pandas as pd

# create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4],
                   'assists': [11, 8, 10, 6, 6, 5, 9, 12]},
                  index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

# view DataFrame
print(df)
print('=' * 50)
print()

# select rows with index labels 'E' and 'F'
print(df.loc[['E', 'F']])
print('=' * 50)
print()

# select 'E' and 'F' rows and 'team' and 'assists' columns
print(df.loc[['E', 'F'], ['team', 'assists']])
print('=' * 50)
print()

# select 'E' and 'F' rows and 'team' and 'assists' columns
print(df.loc['E ':, :' assists'])
print('=' * 50)
print()

# выбор определенных строк DataFrame на основе их целочисленной позиции (6 - не вкл., согласно правилам Python)
print(df.iloc[4:6])
print('=' * 50)
print()

# select rows in range 4 through 6 and columns in range 0 through 2
print(df.iloc[4:6, 0:2])
print('=' * 50)
print()

# select rows from 4 through end of rows and columns up to third column
print(df.iloc[4:, :3])
print('=' * 50)
print()
