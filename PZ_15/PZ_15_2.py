# В матрице найти сумму элементов второй половины матрицы.(столбцы)
import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов: "))
matrix = []
v = column/2
b = 0
for i in range(row):  # Заполнение матрицы
    a = []
    for j in range(column):
        a.append(random.randint(-50, 50))
    matrix.append(a)
for i in range(row):  # Вывод матрицы
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()
for i in range(row):  # Нахождение суммы элементов второй половины матрицы
    for j in range(column):
        if j >= v:
            b += matrix[i][j]
print("Сумма элементов второй половины матрицы: ", b)
