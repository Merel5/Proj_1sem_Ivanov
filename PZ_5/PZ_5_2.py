# Описать функцию Power1(A,B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*In(A)) (параметры A и B - вещественные).В случае нулевого
# или отрицательного параметра A функция возвращает 0.С помощью этой функции
# найти степени A^P,B^P,C^P, если даны числа P,A,B,C.
import math


def power1(a, b):  # Функция
    if a <= 0:
        ab = 0
    else:
        ab = float(math.exp(b*math.log(a, math.e)))
    return ab


A = float(input('Значение A: '))  # Ввод переменных
B = float(input('Значение B: '))
C = float(input('Значение C: '))
P = float(input('Степень A,B,C: '))
print(power1(A, P))  # Вывод результатов
print(power1(B, P))
print(power1(C, P))
