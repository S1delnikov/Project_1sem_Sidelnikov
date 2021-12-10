# Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов.
'''
def pz():
    import random
    from collections import Counter
    n = input('Введите размер списка: ')
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            n = input('Это не число! Попробуйте снова: ')
    k = 1
    N = []
    while k <= n:
        a = random.randint(0, 100)
        N.append(a)
        k+=1
    N = dict(Counter(N))
    print(N)
pz()
'''

import random
n = 100
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input('Это не число! Попробуйте снова: ')
k = 1
N = []
while k <= n:
        a = random.randint(0, 100)
        N.append(a)
        k+=1
print(N)
t = 0
g = 0
s = None
for i in N:
    t = N.count(i)
    if t > g:
        g = t
        s = i
print(s, 'встречается наибольшее количество раз, а именно', t, 'раз')
