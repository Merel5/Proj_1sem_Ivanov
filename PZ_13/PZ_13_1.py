# В последовательности на n целых чисел умножить все элементы на первый элемент
import random


n = int(input('Введите кол-во целых чисел в последовательности: '))
a = []
while n > 0:
    a.append(random.randint(-100, 100))
    n -= 1
print(a)
b = a[0]
с = [b * i for i in a]
print(с)
