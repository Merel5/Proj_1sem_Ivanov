# Из предложенного текстового файла (txt18-16.txt) вывести на экран его
# содержимое, количество букв в верхнем регистре. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив все
# знаки пунктуации на знак <<!>>.
d = 0  # Ввод данных
b = [',', '.', '…', ':', '-', '—', '?', '!', ';']
f2 = open('f.txt', 'w', encoding='UTF-8')
for i in open('text18-16.txt', encoding='UTF-8'):  # Результат
    print(i, end='')
    for j in i:
        if j.isupper():
            d += 1
        a = j
        for t in b:
            if j == t:
                a = j.replace(t, '!')
        f2.write(a)
print(end='\n')
print('Количество букв в верхнем регистре:	', d)
