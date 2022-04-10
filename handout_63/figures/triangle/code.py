def triangle_perimeter(a=7, b=2, c=8):
    p = a + b + c
    return p

def triangle_area(a=7, b=2, c=8):
    p = a + b + c
    from math import sqrt
    h = (2 * sqrt(p * (p - a) * (p - b) * (p - c)))/ a
    s =  a / 2 * h
    return s