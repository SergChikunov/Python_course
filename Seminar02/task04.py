"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

data = [5, 1, 6, 5, 9]
max_elem = data[0]
min_elem = data[1]

for elem in data:
    if elem > max_elem:
        max_elem = elem
    if elem < min_elem:
        min_elem = elem

print(min_elem, max_elem)


def func(data, max_elem=data[1], min_elem=data[1]): # рекурсией
    if len(data) == 0:
        return max_elem, min_elem
    if data[0] > max_elem:
        max_elem = data[0]
    if data[0] < min_elem:
        min_elem = data[0]
    return func(data[1:], max_elem, min_elem)


print(func(data))
