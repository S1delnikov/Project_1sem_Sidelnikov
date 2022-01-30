from tkinter import*

root = Tk()
root.title("Задание 1")
root.geometry('1280x330')

Label(root, text='User login info').place(x=10, y=0)
Label(root, text='Username: ').place(x=10, y =35)
Entry(root, text='username anda').place(x=75, y=35)
Label(root, text='Email: ').place(x=10, y =60)
Entry(root, text='alamat email').place(x=50, y=60)
Label(root, text='Password: ').place(x=10, y=85)
Entry(root).place(x=70, y=85)

Label(root, text='Data diri').place(x=10, y=120)
Label(root, text='Alamat: ').place(x=10, y=145)
Entry(root).place(x=60, y=145)
Label(root, text='Tanggal lahir:').place(x=10, y=170)
Entry(root).place(x=90, y=170)
Label(root, text='Usia:').place(x=10, y=195)
Entry(root).place(x=40, y=195)
Label(root, text='Jenis kelamin:').place(x=10, y=220)
Radiobutton(root, text='Pria', value=1).place(x=90, y=220)
Radiobutton(root, text='Wanita', value=2).place(x=140, y=220)

Label(root, text='Saya bersedia mengikuti aturan forum').place(x=10, y=255)
Checkbutton(root).place(x=220, y=255)

Button(root, text='Reset', width=10).place(x=10, y=280)
Button(root, text='submit', width=10).place(x=95, y=280)
root.mainloop()
