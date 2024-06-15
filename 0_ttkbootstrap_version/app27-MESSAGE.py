from tkinter import *
import ttkbootstrap as ttk

root = ttk.Window()
root.place_window_center()

root.geometry('400x400')

root.title('message')
root['bg']='blue'

texto = Message(root, text='aqui é o texto do message widge',
                font='Arial',
                width=200
                )
texto.pack()

root.mainloop()