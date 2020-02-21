from tkinter import *

def apresentr():
    print('mostrando valor em bit: ', end='')
    print(valor_check.get())

root = Tk()

valor_check = IntVar()

check = Checkbutton(
    root,
    text='isso é uma checkbox',
    variable=valor_check,
    command=apresentr
    ).pack()

root.mainloop()