"""
Файл classmates.csv должен находиться в этой же папке.
Откроем его при помощи Python и прочитаем его содержимое с применением чтения в словарь
Заголовки выводятся отдельной строкой, также подсчитывается количество строк в файле
Использование конструкции with…as придает уверености, что файл будет закрыт, даже если при
выполнении кода произойдет какая-то ошибка.
"""
import csv

with open("classmates.csv", encoding='utf-8') as r_file:  # указываем имя файла и его кодировку
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter=",")
    count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
    for row in file_reader:  # Считывание данных из .csv файла
        if count == 0:  # если count=0, то выводим заголовки столбцов, esle в данной ситуации не требуется - словарь!
            print(f'Файл содержит столбцы: {", ".join(row)}')  # Вывод строки, содержащей заголовки для столбцов
        print(f' {row["Имя"]} - {row["Успеваемость"]} и он родился/родилась в {row["Год рождения"]} году.')  # Вывод строк из файла
        count += 1
    print(f'Всего в файле {count} строк.')
