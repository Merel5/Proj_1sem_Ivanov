# В последовательности на n целых чисел умножить все элементы на первый элемент
from random import randint


n = int(input('Введите кол-во целых чисел в последовательности: '))  # Задание исходной последовательности
a = [randint(-100, 100) for x in range(n)]
print(a)  # Исходная последовательность
b = a[0]
c = [b * i for i in a]
print(c)  # Результат