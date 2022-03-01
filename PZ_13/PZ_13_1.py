# В последовательности на n целых чисел умножить все элементы на первый элемент
import random


n = int(input('Введите кол-во целых чисел в последовательности: '))
a = [x for x in random.randint(-100, 100)]
print(a)
b = a[0]
c = [b * i for i in a]
print(c)
