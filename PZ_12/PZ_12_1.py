# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс
# максимально приближенный к оригиналу
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Workshop Registration")
root.geometry('1200x600')
def button_clicked():
    print("")
def close():
    root.destroy()
    root.quit()


a = Label(text="Register now while seats are available!", fg='red')
a.place(x=2, y=10)
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
