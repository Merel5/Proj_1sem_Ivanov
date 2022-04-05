# В матрице найти сумму элементов второй половины матрицы.
import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов: "))
v = row/2
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]  # Задаём матрицу
print("Матрица: ", matrix)
a = [sum(matrix[j]) for j in range(row) if j >= v]  # Находим сумму второй половины матрицы
b = sum(a)
print("Сумма элементов второй половины матрицы: ", b)
