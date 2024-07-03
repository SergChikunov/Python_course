import csv

# Open the CSV file for reading
with open('employees.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)

    data_list = []  # Инициализация списка для словарей

    for row in csv_reader:
        data_list.append(row)  # вносим каждую строку файла (как словарь) в список

for data in data_list:  # в цикле выводим список словарей
    print(data)
