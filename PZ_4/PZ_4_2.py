# Дано целое число N (>0). Найти сумму 1^1 + 2^2 + ... + N^N.
n = input('Введите число n: ')
i = 1
v = 1
s = 0
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Это не число!')
        n = input('Попробуйте снова! n: ')
while 1 <= n:
    m = v ** v
    s = s + m
    i += 1
    v += 1
    n -= 1
print(s)
