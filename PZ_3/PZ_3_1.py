# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел
# A, B, C являются положительными».

A = input('Введи первое целое число: ')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели')
        A = input('Введи первое целое число: ')
B = input('Введи второе целое число: ')
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Неправильно ввели')
        B = input('Введи второе целое число: ')
C = input('Введи третье целое число: ')
while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print('Неправильно ввели')
        C = input('Введи третье целое число: ')
if ((A > 0) and (B > 0) and (C <= 0)) or ((A <= 0) and (B > 0) and (C > 0)) or ((A > 0) and (B <= 0) and (C > 0)):
    print('Истина')
else:
    print('Ложь')