import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='blue', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='yellow', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='red', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete_records = tk.Button(toolbar, text='Удалить', bg='grey', bd=0, image=self.delete_img,
                                    compound=tk.TOP, command=self.delete_records)
        btn_delete_records.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='green', bd=0, image=self.search_img,
                                       compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='orange', bd=0, image=self.refresh_img,
                               compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, column=('id', 'FN', 'want', 'cost', 'cash'), height=15, show='headings')

        self.tree.column('id', width=10, anchor=tk.CENTER)
        self.tree.column('FN', width=300, anchor=tk.CENTER)
        self.tree.column('want', width=100, anchor=tk.CENTER)
        self.tree.column('cost', width=70, anchor=tk.CENTER)
        self.tree.column('cash', width=70, anchor=tk.CENTER)

        self.tree.heading('id', text='id')
        self.tree.heading('FN', text='ФИО')
        self.tree.heading('want', text='Услуга')
        self.tree.heading('cost', text='Цена')
        self.tree.heading('cash', text='Доход')

        self.tree.pack()

    def records(self, FN, want, cost):
        self.db.insert_data(FN, want, cost)
        self.view_records()

    def update_records(self, FN, want, cost):
        self.db.cur.execute("""UPDATE notus SET FN=?, want=?, cost=? where id=?""",
                            (FN, want, cost, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM notus""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for i in self.tree.selection():
            self.db.cur.execute("""DELETE FROM notus WHERE id=?""", (self.tree.set(i, '#1'), ))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, cost):
        cost = ('%' + cost + '%',)
        self.db.cur.execute("""SELECT * FROM notus WHERE cost LIKE ?""", cost)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_fn = ttk.Label(self, text='ФИО')
        label_fn.place(x=50, y=50)

        label_want = ttk.Label(self, text='Услуга')
        label_want.place(x=50, y=80)

        label_cost = ttk.Label(self, text='Цена')
        label_cost.place(x=50, y=110)

        self.entry_fn = ttk.Entry(self)
        self.entry_fn.place(x=200, y=50)

        self.entry_want = ttk.Entry(self)
        self.entry_want.place(x=200, y=80)

        self.entry_cost = ttk.Entry(self)
        self.entry_cost.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_fn.get(),
                                                                  self.entry_want.get(),
                                                                  self.entry_cost.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редактировать запись')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event:self.view.update_records(self.entry_fn.get(),
                                                                          self.entry_want.get(),
                                                                          self.entry_cost.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть',  command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('notus')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS notus 
            (id integer primary key, FN text, want text, cost real, cash real)""")
        self.conn.commit()
    def insert_data(self, FN, want, cost):
        self.cur.execute("""INSERT INTO notus(FN, want, cost, cash) VALUES (?, ?, ?, ?)""",
                         (str(FN), str(want), int(cost), int(cost)*0.2))
        self.conn.commit()



if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Нотариальная контора")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
