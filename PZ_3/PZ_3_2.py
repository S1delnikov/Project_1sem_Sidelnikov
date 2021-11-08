# Даны два числа. Вывести вначале большее, а затем меньшее из них.
a = input('Введите первое число: ')
while type(a)!=int:
    try:
        a=int(a)
    except ValueError:
        print('Это не число!')
        a = int(input('Попробуйте снова: '))
else:
    b = input('Введите второе число: ')
    while type(b)!=int:
        try:
            b=int(b)
        except ValueError:
            print('Это не число!')
            b = int(input('Попробуйте снова: '))
    else:
        pass
print(a, b, sep=' ; ') if a>b else print(b, a, sep=' ; ')