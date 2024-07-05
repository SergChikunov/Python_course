"""
Задача. Решение в группах. Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной
Условие задачи изменено, работать необходимо с csv файлом, а не txt!
Домашнее задание:
1. Дополнить программу возможностью копирования строки в другой файл csv
2. Организовать валидацию телефонного номера по количеству введенных знаков
"""

from csv import DictWriter, DictReader  # импорт модулей для работы со словарями из библиотеки csv
from os.path import exists  # импорт модуля проверки существования файла


class MyNameError(Exception):  # собственный класс исключений
    def __init__(self, txt):
        self.txt = txt


def get_data():  # функция получения с консоли данных о человеке и его номере телефона
    flag = False  # необходимо для работы цикла, который ниже
    while not flag:  # цикл работает, пока не получит значение False, см. выше
        try:  # проверка валидности вводимых данных
            last_name = input("Введите фамилию: ")
            if len(last_name) < 3:
                raise MyNameError("Слишком короткая фамилия")
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise MyNameError("Слишком короткое имя")
            middle_name = input("Введите отчество: ")
            if len(middle_name) < 5:
                raise MyNameError("Слишком короткое отчество")
            phone = input("Введите номер телефона: ")
            if len(phone) < 11:
                raise MyNameError("Номер телефона должен быть не менее 11 символов")
        except MyNameError as err:  # если исключение сработало, то выводим сообщение об ошибке
            print(err)
        else:
            flag = True  # меняем значение flag на True, соответственно, это означает выход из цикла
    return [last_name, first_name, middle_name, phone]  # по итогу работы функции возвращаем список


def create_file(filename):  # функция создания файла csv
    with open(filename, 'w', encoding='utf-8') as data:  # открываем файл для записи (w) и указываем его кодировку
        f_w = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Телефон'])  # создаем объект DictWriter
        f_w.writeheader()  # пишем в файл заголовки


def read_file(filename):  # функция чтения файла
    with open(filename, 'r', encoding='utf-8') as data:  # открываем файл для записи (r) и указываем его кодировку
        f_r = DictReader(data)  # создаем объект DictWriter
        return list(f_r)  # возвращаем список словарей


def write_file(filename, lst):  # функция записи в файл, filename - имя файла, lst - список из функции get_data()
    res = read_file(filename)  # читаем файл функцией read_file(), получаем список словарей
    obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Отчество': lst[2], 'Телефон': lst[3]}  # формируем значения словаря,
    # используя список
    res.append(obj)  # добавляем сформированный словарь к списку
    standard_write(filename, res)  # записываем изменения в файл при помощи вызова функции standard_write()


def row_search(filename):  # поиск по файлу csv
    res = read_file(filename)  # читаем файл функцией read_file(), получаем список словарей
    print('Сделайте выбор по полю поиска: 1-Фамилия; 2-Имя; 3-Отчество; 4-Телефон')  # что ищем
    f_choice = input("Ваш выбор: ")
    match f_choice:
        case '1':
            criteria = input("Укажите фамилию для поиска: ")
            str = 'Фамилия'
        case '2':
            criteria = input("Укажите имя для поиска: ")
            str = 'Имя'
        case '3':
            criteria = input("Укажите отчество для поиска: ")
            str = 'Отчество'
        case '4':
            criteria = input("Введите номер телефона для поиска: ")
            str = 'Телефон'
        case _:  # если неверно указан критерий, то сработает этот вариант, и не будет ошибки выполнения
            return 'Неверно указан критерий, запустите поиск еще раз!'
    for row in res:  # помним у нас список словарей, проходим по ним в цикле
        if criteria == row[str]:  # сравниваем значение того что ищем (last_name)
            # со значением словаря по ключу Фамилия
            return row  # возвращаем найденный словарь, он же одна строка из файла, он же одна запись файла
    return "Запись не найдена"  # возвращаем это, если не нашли ничего подходящего


def delete_row(filename):  # функция удаления строки из файла
    row_number = int(input("Введите номер строки: "))  # номер строки в целочисленном формате
    res = read_file(filename)  # читаем файл функцией read_file(), получаем список словарей
    res.pop(row_number - 1)  # удаляем словарь с номером меньше чем row_number на 1, т.к. индексы списка стартуют с 0
    standard_write(filename, res)  # записываем изменения в файл при помощи вызова функции standard_write()


def standard_write(filename, res):  # функция записи в файл csv, res - список из функции get_data()
    with open(filename, 'w', encoding='utf-8') as data:  # открываем файл для записи (w) и указываем его кодировку
        f_w = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Телефон'])  # создаем объект DictWriter
        f_w.writeheader()  # пишем в файл заголовки
        f_w.writerows(res)  # пишем строки, res - список словарей, каждый из которых - отдельная строка файла


def change_row(filename):  # функция изменения строки в csv файле
    row_number = int(input("Введите номер строки: "))  # номер строки в целочисленном формате
    res = read_file(filename)  # читаем файл функцией read_file(), получаем список словарей
    data = get_data()  # вызываем функцию get_data() и получаем список словарей
    res[row_number - 1]["Фамилия"] = data[0]  # меняем все данные в указанной выше строке, переменная row_number
    res[row_number - 1]["Имя"] = data[1]
    res[row_number - 1]["Отчество"] = data[2]
    res[row_number - 1]["Телефон"] = data[3]
    standard_write(filename, res)  # записываем изменения в файл при помощи вызова функции standard_write()


def copy_row(filename, other_filename):  # функция копирования строки из одного csv файла в другой
    res = read_file(other_filename)  # читаем файл функцией read_file(), получаем список словарей
    find_result = row_search(filename)
    if find_result == "Запись не найдена":
        return print("Нет такой строки в исходном файле! Следует проверить правильность ввода!")
    else:
        res.append(find_result)
        standard_write(other_filename, res)  # пишем изменения в файл при помощи вызова функции standard_write()


def main():  # основной модуль с которого начинает работу программа
    while True:  # бесконечный цикл, в котором ожидаем реакции с консоли
        print('Сделайте выбор: "q"- завершение; "w"-запись csv; "r"-чтение csv; "f"-поиск в csv', end=';')
        print(' "d"-удаление из csv; "c"-изменить строку в csv; "k"-копирование строки в другой файл csv')
        choice = input("Укажите ваш выбор: ").lower()
        match choice:
            case "q":  # выход из программы
                break
            case "w":  # запись данных в csv файл
                if not exists(filename):  # если файл с указанным именем не существует,
                    create_file(filename)  # то создаем его, вызвав функцию create_file()
                write_file(filename, get_data())
            case "r":  # чтение csv файла
                if not exists(filename):
                    print("Файл не существует. Создайте его.")
                    continue
                # выведем список словарей в виде принятом для csv
                list_res = (read_file(filename))
                print(*list_res[0])
                for i in range(len(list_res)):
                    print(list_res[i]['Фамилия'], list_res[i]['Имя'], list_res[i]['Отчество'], list_res[i]['Телефон'])
            case "f":  # поиск строки в csv файле
                if not exists(filename):
                    print("Файл не существует. Создайте его.")
                    continue
                print(row_search(filename))
            case "d":  # удаление строки в csv файле
                if not exists(filename):
                    print("Файл не существует. Создайте его.")
                    continue
                delete_row(filename)
            case "c":  # изменение строки в csv файле
                if not exists(filename):
                    print("Файл не существует. Создайте его.")
                    continue
                change_row(filename)
            case "k":  # копирование строки из одного csv файла в другой
                if not exists(filename):
                    print("Файл не существует, копировать нечего! Создайте файл и запишите в него данные!")
                    continue
                copy_row(filename, other_filename)


filename = 'phone.csv'  # задаем имя файла csv в переменную
other_filename = 'phoneTwo.csv'  # имя файла приемника копируемых данных
main()  # вызов функции с основным модулем выбора
