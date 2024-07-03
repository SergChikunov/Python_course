import csv

fields = ['Name', 'Branch', 'Year', 'CGPA']  # имена полей
# данные, которые будут помещены в строки записываемого файла
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

filename = "university_records.csv"  # имя файла

with open(filename, 'w') as csvfile:  # открытие файла для записи
    csvwriter = csv.writer(csvfile)  # создание объекта csv.writer
    csvwriter.writerow(fields)  # запись полей
    csvwriter.writerows(rows)  # запись данных в строки
