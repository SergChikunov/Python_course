my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# традиционный итератор с методом add()
unique_values = set()
for item in my_list:
    for value in item.values():
        unique_values.add(value)
print(unique_values)

# формируем множество при помощи set comprehension, если убрать set, то это генератор???
print(set(value for item in my_list for value in item.values()))
