# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое, количество символов в тексте.
# Сформировать новый файл, в который поместить строку наибольшей длины.

borodino = ['Вам не видать таких сражений!..',
            'Носились знамена, как тени,',
            'В дыму огонь блестел,',
            'Звучал булат, картечь визжала,',
            'Рука бойцов колоть устала,',
            'И ядрам пролетать мешала',
            'Гора кровавых тел.']

lermontov_1 = open('borodino_1.txt', 'w')
for i in borodino:
    lermontov_1.write(i + '\n')
lermontov_1.close()

lermontov_1 = open('borodino_1.txt', 'r')
print(lermontov_1.read())
print(f'Количество символов в тексте: {len(str(borodino))}')
lermontov_1.close()

lermontov_2 = open('borodino_2.txt', 'w')
stroka = ''
for i in borodino:
    stroka = stroka if len(stroka) > len(i) else i
lermontov_2.write(stroka)
lermontov_2.close()

lermontov_2 = open('borodino_2.txt', 'r')
print('Строка наибольшей длины: ' + '\n' + lermontov_2.read())
lermontov_2.close()
