# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 3 – 8.
# Я выбрал задачу из ПЗ № 8, вот её условие:
# Используя словарь подсчитать количество уникальных слов в заданном предложении. Вывести на экран
# каждую пару "ключ:значение".

from tkinter import *

tk = Tk()
tk.title("Задание 2")
tk.geometry('500x100')

def uniq():
    stroke = vvod.get()
    d = stroke.split()
    d1 = {}
    for i in d:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    vivod_1['text'] = f"Счётчик повторений слов: {d1}"
    k = 0
    for i in d1:
        if d1[i] == 1:
            k += 1
    vivod_2['text'] = f"Количество уникальных слов: {k}"

Label(text='Поле ввода: ').grid(row=1, column=0)
vvod = Entry(width='50')
vvod.grid(row=1, column=1, sticky='w')

Button(text='Найти уникальные элементы', bg='#00FF00', activebackground='#ffff00',
       command=uniq).grid(row=2, column=1, sticky='w')

Label(text='Поле вывода: ').grid(row=3, column=0)

vivod_1 = Label()
vivod_1.grid(row=3, column=1, sticky='w')

vivod_2 = Label()
vivod_2.grid(row=4, column=1, sticky='w')

tk.mainloop()
