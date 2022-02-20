# Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.

import string

str = 'In PyCharm, you can specify third-patry ' \
      'standalone applications and run them as ' \
      'External Tools'
symb = [' ', '-', '.', ':', ';','"']
lst = [n for n in str if n in string.ascii_lowercase
       or n in symb]
print(str)
print('_' * 100)
print(''.join(lst))
