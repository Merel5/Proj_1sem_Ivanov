# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]
print(matrix)
s = [sum(matrix[i]) for i in range(column)]
print(s)
