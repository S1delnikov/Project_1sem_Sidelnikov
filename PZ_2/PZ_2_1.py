# Дано трёхзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа
# (например, 123 перейдёт в 213)
try:
    k = int(input('Введите трёхзначное : '))
    a = (k // 100) * 10
    b = (k // 10) % 10 * 100
    c = k % 10
    if (k>999) or (k<100): # Проверка на ввод трёхзначного числа
        print('Вы ввели не трёхзначное число, попробуйте снова')
    else:
        if b == 0: # Если десятки равны нулю, то в начале полученного числа он писаться не будет
            print(a + c)
        else: # Если десятки от 1 до 9, то выполняем программу, как обычно
            print(b + a + c)
except ValueError: # Если пользователь вводит текст, то при ошибке будет выводиться сообщение об ошибке
    print('Вы ввели не число')



