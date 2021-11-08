# Дано вещественное число X и целое число N(>0). Найти значение  выражения 1 - X^2/(2!) + X^4/(4!) - ... + (-1)^n -
# - X^(2*N)/((2-N)!) (N! = 12 ... N). Полученное число является приближённым значением функции cos в точке X.

n = input('Введите число n: ')
i = 1
k = 1
v = 0
cos = 0
fact = 1
g = 2
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Введите целое число!')
        n = input('n: ')
x = input('Введите число x: ')
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print('Введите вещественное число!')
        x = input('x: ')
while i <= n:
    v += 2
    while k <= g:
        fact *= k
        k += 1
    g += 2
    m = x ** v / fact
    if i % 2 == 1:
        cos = cos + m
    else:
        cos = cos - m
    i += 1
    d = 1 - cos
print('Приближённое значение функции cos в точке x: ', d)
