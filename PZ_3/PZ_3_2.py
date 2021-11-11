# Даны три целых числа, одно из которых отлично от двух других, равных между собой.
# Определить порядковый номер числа, отличного от остальных.

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
if A != B and B == C and A != C:
    print('Отличное от остальных первое')
elif A != B and B != C and A == C:
    print('Отличное от остальных второе')
elif A == B and B != C and A != C:
    print('Отличное от остальных третье')
elif A != B and B != C and A != B:
    print('Все отличаются друг от друга')
elif A == B and B == C and A == B:
    print('Все одинаковые')
