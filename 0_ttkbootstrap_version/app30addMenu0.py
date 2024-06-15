# 038 - Python tkinter - ADICIONAR MENUS À APLICAÇÃO
from tkinter import *
import ttkbootstrap as ttk


root = ttk.Window()
root.style.theme_use('darkly')
root.place_window_center()

root.geometry('300x300')

def file():
    print('file')

meuMenu = ttk.Menu(root )

meuMenu.add_command(label='file', command=file)
meuMenu.add_command(label = 'edit')

root.config(menu = meuMenu)

root.mainloop()