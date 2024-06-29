"""
Файлы в текстовом формате используются для:
● Хранения данных
● Передачи данных в клиент-серверных проектах
● Хранения конфигов
● Логирования действий
Что нужно для работы с файлами:
1. Завести переменную, которая будет связана с этим текстовым файлом.
2. Указать путь к файлу.
3. Указать, в каком режиме мы будем работать с файлом.
Варианты режима (мод):
1. a – открытие для добавления данных.
        Позволяет дописывать что-то в имеющийся файл.
        Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан и в него начнётся запись.
2. r – открытие для чтения данных.
        Позволяет читать данные из файла.
        Если вы попробуете считать данные из файла, которого не существует, программа выдаст ошибку.
3. w – открытие для записи данных.
        Позволяет записывать данные и создавать файл, если его не существует.
Миксованные режимы:
4. w+
        Позволяет открывать файл для записи и читать из него.
        Если файла не существует, он будет создан.
5. r+
        Позволяет открывать файл для чтения и дописывать в него.
        Если файла не существует, программа выдаст ошибку.
"""

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')  # здесь указываем режим, в котором будем работать
# data.writelines(colors)  # разделителей не будет
# data.close()


with open('file.txt', 'w') as data:
    data.write('This is a first row in the file\n')
    data.write('This is a second row in the file\n')


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()