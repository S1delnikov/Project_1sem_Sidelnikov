# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделённых пробелами (одним или несколькими).
# Преобразовать каждое слово в строке, заменив в нём все последующие вхождения его первой буквы на символ "." (точка).
# Например, слово "МИНИМУМ" надо преобразовать в "МИНИ.У.". Количество пробелов между слов не изменять.

def new(x):
    fst = x[0]
    return x.replace(fst, '.').replace('.', fst, 1)
# n = input('Введите слово или предложение: ')
n = 'ПЕРСПЕКТИВНО ИМПОРТИРОВАНИЕ     ВДОВА'
lst = n.split()
for i in lst:
    n = n.replace(i, new(i))
print(n)
