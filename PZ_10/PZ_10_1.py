# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

chisla = ['-1 21 35 6 -7 3 -51 -9']

f1 = open('info.txt', 'w')
f1.writelines(chisla)
f1.close()

f2 = open('info_copy.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(chisla)
f2.close()

f1 = open('info.txt')    # Вычисляю количество элементов, числа кратные трём и количество чисел кратных трём
k = f1.read()
k = k.split()
crat = []
for i in range(len(k)):
    k[i] = int(k[i])
    if k[i] % 3 == 0:
        crat.append(k[i])
crat_count = len(crat)
f1.close()

f1 = open('info.txt')    # Вычисляю минимальный элемент
min, t = 0, 0
for i in range(len(k)):
    min = min if min < k[i] else k[i]
    if k[i] < 0:
        t += 1
f1.close()

f2 = open('info_copy.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(k), '\n', 'Минимальный элемент: ', min, '\n', 'Числа кратные трём: ', crat,
      '\n', 'Количество чисел кратных трём: ', crat_count, file=f2)
f2.close()

f1 = open('info.txt')
f2 = open('info_copy.txt')
print('Первый файл: ', '\n', f1.read())
print('Второй файл: ', '\n', f2.read())
f1.close()
f2.close()
