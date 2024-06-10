"""
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.

Пример:


n = 123 -> res = 6 (1 + 2 + 3)

n = 100 -> res = 1 (1 + 0 + 0)
"""
n = 355

# firstDigit = n // 100
# thirdDigit = n % 10
# secondDigit = n // 10 % 10
res = n // 100 + n % 10 + n // 10 % 10
# print(firstDigit)
# print(thirdDigit)
# print(secondDigit)
print(res)
