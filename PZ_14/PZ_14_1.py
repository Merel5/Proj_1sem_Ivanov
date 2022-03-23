# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.
import re

p = re.compile(r"[0-9]+ руб\. [0-9]+ коп\.")
with open('price.txt', 'r', encoding="utf-8") as file:
    text = file.read()
    i = len(re.findall(p, text))
print(re.findall(p, text))
print(i)
