# Разработать программу с применением пакета tk по условию: Найти сумму чисел
# ряда 1,2,3,4,... от числа n до m. Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.
from tkinter import *
def close():
    root.destroy()
    root.quit()
def jet(a, b):
    k = 0
    b += 1
    while a < b:
        k += a
        a += 1
    return k


root = Tk()
root.title("Summary")
root.geometry('500x400')
a1 = Label(text="Задать числа n и m для суммирования всех чисел между ними")
a1.place(x=2, y=5)
a2 = Label(text="n")
a2.place(x=2, y=30)
a3 = Label(text="m")
a3.place(x=80, y=30)
n = Entry(width="4")
n.place(x=20, y=30)
m = Entry(width="4")
m.place(x=100, y=30)
e1 = Entry.get(n)
e2 = Entry.get(m)
e1 = int(e1)
e2 = int(e2)
s2 = Button(root, text='Sum', width=10, height=1, command=jet(e1, e2))
s2.place(x=80, y=60)
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
