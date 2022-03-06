# В матрице найти сумму элементов первых двух строк.

from random import randint

strok = int(input('Введите количество строк в матрице: '))
stolb = int(input('Введите количество столбцов в матрице: '))
mat = [[randint(0, 10) for i in range(stolb)] for j in range(strok)]
print(f"Матрица: ")

for i in mat:
    print(str(i))

double = [i for i in mat[:2][:]]
print(f"Первые две строки матрицы: {double}")
plus = [sum(i) for i in double[:][:]]
print(f'Сумма элементов первых двух строк: {sum(plus)}')
