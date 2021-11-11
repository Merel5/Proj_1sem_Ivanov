# Дано вещественное число A и целое число N (N>0). Используя один цикл, найти значение
# выражения 1 - A + A 2 - A 3 + ... +(-1) N A N . Условный оператор не использовать.

A = float(input('Введите вещественное число: '))
while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print('Неправильно ввели')
        A = input('Введите вещественное число: ')
N = input('Введите целое число больше ноля: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели')
        N = input('Введите целое число больше ноля: ')
while N < 0:
    print('Неправильно ввели')
    N = input('Введите целое число больше ноля: ')
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print('Неправильно ввели')
            N = input('Введите целое число больше ноля: ')
C = 0
j = 0
K = -1
while K < N:
    a = (pow(-1, C))
    b = (pow(A, C))
    h = a * b
    j += h
    C += 1
    K += 1
print('Результат =', j)
