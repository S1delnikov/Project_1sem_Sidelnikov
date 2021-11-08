# Проверить истинность высказывания: "Среди трёх данных целых чисел есть хотя бы одна пара взаимно противоположных"

a, b, c = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')
try:
    a = int(a)
except ValueError:
    print('Неправильно ввели первое число')
try:
    b = int(b)
except ValueError:
    print('Неправильно ввели второе число')
try:
    c = int(c)
except ValueError:
    print('Неправильно ввели третье число')
if (a == b * -1):
    print('Истинно')
elif(a == c * -1):
    print('Истинно')
elif (b == a * -1):
    print('Истинно')
elif(b == c * -1):
    print('Истинно')
elif (c == a * -1):
    print('Истинно')
elif(c == b * -1):
    print('Истинно')
else:
    print('Ложно')
