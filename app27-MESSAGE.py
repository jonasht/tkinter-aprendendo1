from tkinter import *

root = Tk()
root.geometry('400x400+600+300')
root.title('message')
root['bg']='blue'

texto = Message(root, text='aqui é o texto do message widge',
                font='Arial',
                width=200
                )
texto.pack()

root.mainloop()