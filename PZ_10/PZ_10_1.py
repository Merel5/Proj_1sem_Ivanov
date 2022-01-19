# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных чисел и отрицательных чисел.
# Сформировать новый текстовый файл(.txt) следующего вида, предварительно
# выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Положительные числа:
# Количество положительных чисел:
# Отрицательные числа:
# Количество отрицательных чисел:
import random


c = 0
v = 0
a = []
b = random.randint(1, 12)
while b > 0:
    a.append(random.randint(-100, 100))
    b -= 1
a = str(a)
f1 = open('numbers.txt', 'w', encoding='UTF-8')
f1.writelines(a)
a = a.replace('[', '')
a = a.replace(']', '')
a = a.split(',')
f2 = open('results.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные:')
f2.writelines(a)
f2.write('\n')
f2.write('Количество элементов:')
f2.write((str(len(a))))
f2.write('\n')
f2.write('Положительные числа:')
for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] > 0:
        f2.write(str(a[i]))
        f2.write(' ')
    if a[i] > 0:
        c += 1
f2.write('\n')
f2.write('Количество положительных чисел:')
f2.write(str(c))
f2.write('\n')
f2.write('Отрицательные числа:')
for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] < 0:
        f2.write(str(a[i]))
        f2.write(' ')
    if a[i] < 0:
        v += 1
f2.write('\n')
f2.write('Количество отрицательных чисел:')
f2.write(str(v))
