# 038 - Python tkinter - ADICIONAR MENUS À APLICAÇÃO
from tkinter import *

root = Tk()
root.geometry('300x300')

def file():
    print('file')

meuMenu = Menu(root )

meuMenu.add_command(label='file', command=file)
meuMenu.add_command(label = 'edit')

root.config(menu = meuMenu)

root.mainloop()