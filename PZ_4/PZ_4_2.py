# Даны положительные числа A и B (A > Б). На отрезке длины A размещено максимально
# возможное количество отрезков длины B (без наложений). Не используя операции
# умножения и деления, найти количество отрезков Б, размещенных на отрезке A.

A = input('Введите длину отрезка A: ')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели')
        A = input('Введите длину отрезка A: ')
while A < 0:
    print('Неправильно ввели')
    A = input('Введите длину отрезка A: ')
    while type(A) != int:
        try:
            A = int(A)
        except ValueError:
            print('Неправильно ввели')
            A = input('Введите длину отрезка A: ')
B = input('Введите длину отрезка B,которая меньше A: ')
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Неправильно ввели')
        B = input('Введите длину отрезка B: ')
while B < 0:
    print('Неправильно ввели')
    B = input('Введите длину отрезка B: ')
    while type(B) != int:
        try:
            B = int(B)
        except ValueError:
            print('Неправильно ввели')
            B = input('Введите длину отрезка B: ')
while A < B:
    print('Неправильно ввели')
    A = input('Введите длину отрезка A: ')
    while type(A) != int:
        try:
            A = int(A)
        except ValueError:
            print('Неправильно ввели')
            A = input('Введите длину отрезка A: ')
    while A < 0:
        print('Неправильно ввели')
        A = input('Введите длину отрезка A: ')
        while type(A) != int:
            try:
                A = int(A)
            except ValueError:
                print('Неправильно ввели')
                A = input('Введите длину отрезка A: ')
    B = input('Введите длину отрезка B: ')
    while type(B) != int:
        try:
            B = int(B)
        except ValueError:
            print('Неправильно ввели')
            B = input('Введите длину отрезка B: ')
    while B < 0:
        print('Неправильно ввели')
        B = input('Введите длину отрезка B: ')
        while type(B) != int:
            try:
                B = int(B)
            except ValueError:
                print('Неправильно ввели')
                B = input('Введите длину отрезка B: ')
C = 0
c = 0
while C < A:
    C += B
    if C < A:
        c += 1
print('Количество отрезков B на отрезке A =', c)