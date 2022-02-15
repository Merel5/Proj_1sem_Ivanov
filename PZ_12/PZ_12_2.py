# Разработать программу с применением пакета tk по условию: Найти сумму чисел
# ряда 1,2,3,4,... от числа n до m. Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.
from tkinter import *  # импортирую библиотеку


def close():  # Функции
    root.destroy()
    root.quit()
def jet():
    try:
        a = int(n.get())
        b = int(m.get())
        k = 0
        b += 1
        while a < b:
            k += a
            a += 1
        a4.config(text="Результат {}".format(k))
    except ValueError:
        a4.config(text="Ошибка введите цифры")


root = Tk()  # Виджеты
root.title("Summary")
root.geometry('500x400')
a1 = Label(root, text="Задать числа n и m для суммирования всех чисел между ними")
a1.place(x=2, y=5)
a2 = Label(root, text="n")
a2.place(x=2, y=30)
a3 = Label(root, text="m")
a3.place(x=80, y=30)
c1 = IntVar()
c2 = IntVar()
n = Entry(root, width="4", textvariable=c1)
c1.set(0)
n.place(x=20, y=30)
m = Entry(root, width="4", textvariable=c2)
c2.set(0)
m.place(x=100, y=30)
s2 = Button(root, text='Sum', width=10, height=1, command=jet)
s2.place(x=80, y=60)
a4 = Label(text="Результат")
a4.place(x=140, y=30)
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
