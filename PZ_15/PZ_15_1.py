# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]  # Задаём матрицу
print("Матрица: ", matrix)
s = [sum(matrix[j]) for j in range(row)]  # Находим суммы строк
print("Суммы строк: ", s)
a = [matrix[j].insert(2, s[j]) for j in range(row)]  # Редактируем матрицу
b = [matrix[j].pop(3) for j in range(row)]
print("Отредактированная матрица: ", matrix)
