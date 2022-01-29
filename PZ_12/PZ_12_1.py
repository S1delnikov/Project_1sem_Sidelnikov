from tkinter import*

root = Tk()
root.title("Задание 1")
root.geometry('1280x400')

Label(root, text='User login info').place(x=0, y=0)    #User login info
Label(root, text='Username: ').place(x=0, y =35)
Entry(root, text='username anda').place(x=65, y=35)
Label(root, text='Email: ').place(x=0, y =60)
Entry(root, text='alamat email').place(x=40, y=60)
Label(root, text='Password: ').place(x=0, y=85)
Entry(root).place(x=60, y=85)

Label(root, text='Data diri').place(x=0, y=120)
Label(root, text='Alamat: ').place(x=0, y=145)
Entry(root).place(x=50, y=145)
Label(root, text='Tanggal lahir:').place(x=0, y=170)
Entry(root).place(x=80, y=170)
Label(root, text='Usia:').place(x=0, y=195)
Entry(root).place(x=30, y=195)
Label(root, text='Jenis kelamin:').place(x=0, y=220)
Radiobutton(root, text='Pria').place(x=80, y=220)
Radiobutton(root, text='Wanita').place(x=130, y=220)

Label(root, text='Saya bersedia mengikuti aturan forum').place(x=0, y=255)
Radiobutton(root).place(x=210, y=255)

Button(root, text='Reset').place(x=10, y=280)

root.mainloop()

