"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_person(**person_data):
    print(f"Контактное лицо: {person_data['last_name']} {person_data['name']}, {person_data['birth']} года рождения, "
          f"проживает в городе {person_data['city']}, адрес e-mail: {person_data['email']}, "
          f"номер телефона: {person_data['phone']}")


print_person(name="Иван", last_name="Иванов", birth="1984", city="Ростов", email="ivanovovan007@hotmail.com",
             phone="154682446222")
print_person(name="Николай", last_name="Васенин", birth="1999", city="Москва", email="vaseninkolya1999@yandex.com",
             phone="+74955556711")
