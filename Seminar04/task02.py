"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13

Если вводить текст по правилам, то следует после точки ставить пробел.
В этом случае результат решения меняется, если убрать точку после sure,
тогда результат будет как в условии!
Можно еще удалить точку из строки, тогда результат уже будет соответствовать
заданному в условии.
"""

str_input = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

my_str = str_input.lower()
my_iter = 0
# удаление точки из строки
for i in range(len(my_str)):
    if my_str[i] == '.':
        my_iter = i
left_half = my_str[:my_iter]
right_half = my_str[my_iter + 1:]
my_str = left_half + right_half
print(my_str)
# завершение части кода который удаляет точку из строки
new_list = my_str.split(' ')  # список оставлен для подсчета общего количества слов в тексте
new_set = set(my_str.split(' '))
print(f'Всего в тексте {len(new_list)} слов')
print(new_set)
print(f'Различных слов в тексте: {len(new_set)}')