# Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию. Сделать список упорядоченным,
# переместив элемент, нарушающий упорядоченность, на новую позицию.
import random
lst = []
k = 1
n = input('Введите размер списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input('Это не число! Попробуйте снова: ')
while k<=n:
    lst.append(random.randint(0, 100))
    k+=1
lst.sort(reverse=True)
lst.insert(random.randint(0, len(lst)), lst[-1])    # создаю список список из условия задачи
lst.pop(-1)
def rlst():    # решение задачи
    lst.sort(reverse=True)
    print(lst)
rlst()