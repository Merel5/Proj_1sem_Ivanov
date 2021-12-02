# Дан список A размера N. Вывести его элементы в следующем порядке:A1,
# A2,AN,AN-1,A3,A4,AN-2,AN-3,... .
import random


a = 0
N = int(input('Размер списка: '))
t = int(N)
A = []
p = N
N -= 1
while t:
    A.append(random.randint(-100, 100))
    t -= 1
print(A)
while p:
    if a <= N:
        print(A[a])
        a += 1
    if a <= N:
        print(A[a])
        a += 1
    if a <= N:
        print(A[N])
        N -= 1
    if a <= N:
        print(A[N])
        N -= 1
    p -= 1
