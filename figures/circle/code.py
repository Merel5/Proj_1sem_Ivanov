from math import pi


def circle_perimeter(r):
    c = 2*r*pi
    return c


def circle_area(r):
    s = pi*r*r
    return s


r = 5
print(circle_perimeter(r))
print(circle_area(r))
