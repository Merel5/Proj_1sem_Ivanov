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


a = []
b = random.randint(1, 12)
while b > 0:
    a.append(random.randint(-100, 100))
    b -= 1
a = str(a)
f1 = open('numbers.txt', 'w', encoding='UTF-8')
f1.writelines(a)
a = a.split()
print(a)
f2 = open('results.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные:')
f2.writelines(a)
f2.write('Количество элементов:')
