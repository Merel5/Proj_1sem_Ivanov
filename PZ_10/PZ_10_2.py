# Из предложенного текстового файла (txt18-16.txt) вывести на экран его
# содержимое, количество букв в верхнем регистре. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив все
# знаки пунктуации на знак <<!>>.
t = 0
d = 0
f2 = open('f.txt', 'w', encoding='UTF-8')
for i in open('text18-16.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        if j.isupper():
            d += 1
    if i.isalnum:
        f2.write(i)
    else:
        f2.write(i.replace('!', '!'))
    if i.isalnum:
        f2.write(i)
    else:
        f2.write(i.replace(',', '!'))
    if i.isalnum:
        f2.write(i)
    else:
        f2.write(i.replace('.', '!'))
    if i.isalnum:
        f2.write(i)
    else:
        f2.write(i.replace(':', '!'))
print(end='\n')
print('Количество букв в верхнем регистре:	', d, end='\n')
