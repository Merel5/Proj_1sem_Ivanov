# Найти сумму чисел ряда 1,2,3,4,... от числа n до m. Суммирование
# оформить функцией с параметрами. Значения n и m программа должна
# запрашивать.

def jet(a, b):  # Функция
    k = 0
    b += 1
    while a < b:
        k += a
        a += 1
    return k


n = int(input('Ввести значение первой цифры: '))  # Ввод переменных
m = int(input('Ввести значение второй цифры: '))
print(jet(n, m))  # Вывод суммы
