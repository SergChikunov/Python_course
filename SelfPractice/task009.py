import csv

# csv file name
filename = "aapl.csv"

# Инициализация списков для имен полей и строк
fields = []
rows = []

with open(filename, 'r') as csvfile:  # чтение csv файла
    csvreader = csv.reader(csvfile)  # создание объекта csv reader

    fields = next(csvreader)  # извление имен полей из первой строки в соответствующий список

    for row in csvreader:  # последовательное чтение строк файла
        rows.append(row)

    print("Total no. of rows: %d" % (csvreader.line_num))  # печать общего количества строк в файле

# вывод имен полей с использованием метода join() и генератора списка
print('Field names are:' + ', '.join(field for field in fields))

print('\nFirst 5 rows are:\n')  # вывод первых 5 строк из файла csv
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" "),  # форматируем каждый столбец строки
    print('\n')
