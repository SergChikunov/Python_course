n = int(input('Введите числовое значение и нажмите Enter... '))
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1