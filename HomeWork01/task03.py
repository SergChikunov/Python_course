"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
Пример:

n = 385916 -> yes
n = 123456 -> no
"""

n = 555555
leftHalf = n // 1000
rightHalf = n % 1000
# print(leftHalf, ' ', rightHalf) # для отладки
tempSumLeftHalf = leftHalf // 100 + leftHalf % 10 + leftHalf // 10 % 10
tempSumRightHalf = rightHalf // 100 + rightHalf % 10 + rightHalf // 10 % 10
# print(tempSumLeftHalf, ' ', tempSumRightHalf) # для отладки
print('Yes' if tempSumLeftHalf == tempSumRightHalf else 'No')
