# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
import random


def q():
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()


row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = []
matrix2 = []
for i in range(row):
    a = []
    for j in range(column):
        a.append(random.randint(-50, 50))
    matrix.append(a)
q()
for i in range(row):
    b = 0
    for j in range(column):
        b += matrix[i][j]
    matrix2.append(b)
print(matrix2)
for i in range(row):
    for j in range(column):
        if j == 2:
            matrix[i][j] = matrix2[i]
q()
