import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="12.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="14.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="15.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('instruction_id', 'name', 'data', 'term', 'executioner'), height=15,
                                 show='headings')

        self.tree.column('instruction_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('data', width=140, anchor=tk.CENTER)
        self.tree.column('term', width=140, anchor=tk.CENTER)
        self.tree.column('executioner', width=140, anchor=tk.CENTER)

        self.tree.heading('instruction_id', text='Порядковый номер поручения')
        self.tree.heading('name', text='Название поручения')
        self.tree.heading('data', text='Дата выдачи поручения')
        self.tree.heading('term', text='Срок исполнения')
        self.tree.heading('executioner', text='Исполнитель')

        self.tree.pack()

    def records(self, instruction_id, name, data, term, executioner):
            self.db.insert_data(instruction_id, name, data, term, executioner)
            self.view_records()

    def update_record(self, instruction_id, name, data, term, executioner):
        self.db.cur.execute("""UPDATE instructions SET instruction_id=?, name=?, data=?, term=?, executioner=? WHERE 
        instruction_id=?""", (instruction_id, name, data, term, executioner, self.tree.set(self.tree.selection()[0],
                                                                                           '#1')))
        self.db.con.commit()
        self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM instructions WHERE instruction_id=?""",
                                (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM instructions""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, executioner):
        executioner = ("%" + executioner + "%",)
        self.db.cur.execute("""SELECT * FROM instructions WHERE executioner LIKE ?""", executioner)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_search_dialog(self):
        Search()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить поручение')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер поучения')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=170, y=25)

        label_name = tk.Label(self, text='Название')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=170, y=50)

        label_sex = tk.Label(self, text='Дата выдачи')
        label_sex.place(x=50, y=75)
        self.combobox = ttk.Entry(self)
        self.combobox.place(x=170, y=75)

        label_old = tk.Label(self, text='Срок сдачи')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=170, y=100)

        label_score = tk.Label(self, text='Исполнитель')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=170, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_score.get()))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):

        with sq.connect('instructions.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS instructions(
                instruction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                data TEXT,
                term TEXT,
                executioner TEXT NOT NULL
                )""")

    def insert_data(self, instruction_id, name, data, term, executioner):
        self.cur.execute("""INSERT INTO instructions(instruction_id, name, data, term, executioner) 
        VALUES (?, ?, ?, ?, ?)""", (instruction_id, name, data, term, executioner))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Контроль исполнения поручений')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
