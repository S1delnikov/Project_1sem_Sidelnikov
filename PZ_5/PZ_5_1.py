# Составить функцию, которая напечатает 40 любых символов.
a = input('Введите любой символ: ')
def spam(a, b = []):
    k = 1
    while k<=40:
        b.append(a)
        k+=1
    print(b)
spam(a)


