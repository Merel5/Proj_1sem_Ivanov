from math import sqrt


def triangle_perimetr(a, b, c):
    q = a + b + c
    print(q)


def triangle_area(a, b, c):
    w = sqrt((a+b+c)/2*(((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c)))
    print(w)


a = 7
b = 2
c = 8
triangle_perimetr(a, b, c)
triangle_area(a, b, c)
