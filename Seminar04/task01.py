"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

input_str = 'a a a b c a a d c d d'

my_list = input_str.split(' ')
print(my_list)

for i, elem in enumerate(my_list):  # с помощью enumerate удобно одновременно получить индекс и значение элемента
    # print('i =', i, 'value =', elem) # использовал для отладки, дает понимание как работает enumerate
    counter = 1  # это счетчик для нумерации количества вхождений элемента в список
    k = 0  # это счетчик цикла while, для каждой итерации for он начинается заново
    while k < len(my_list):
        # print(my_list[k]) # использовал для отладки
        if k != i and elem == my_list[k]:  # если k не равен i, а значение элемента от i равно элементу списка от k, выполняем условие
            tmp = my_list.pop(k) + '_' + str(counter)  # удаляем элемент от k из списка, конкатенируем к нему символ _ и значение счетчика counter, предварительно сконвертировав его в строку, и всю строку сохраняем в tmp
            my_list.insert(k, tmp)  # вставляем tmp в список, на позицию k
            counter += 1  # счетчик counter увеличиваем именно в конце работы if
        k += 1  # как упоминалось выше - это счетчик while
print(my_list)  # выводим результат



input_string = "a a a b c a a d c d d"
words = input_string.split()
counts = {}

for word in words:
    if word not in counts:
        print(word, end=' ')
    else:
        print(f"{word}_{counts[word]}", end=' ')
    counts[word] = counts.get(word, 0) + 1