# Сгенерировать словарь вида  {0:0,1:1,2:4,3:9,4:16,5:25,6:36}, удалить из
# него второй и третий элементы. Отобразить исходный и получившийся словарь.
# Использовать for, range.
A = {}
a = 0
b = 0
for a in range(0, 7):
    b = a
    b *= b
    A[a] = b
print(A)
A.pop(1)
A.pop(2)
print(A)
