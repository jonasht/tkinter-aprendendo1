from tkinter import *

root = Tk()

root.title('log in')
Label(root, text='usuario:').grid(row=0, sticky=W)
Label(root, text='Senha:').grid(row=1, sticky=W)


text_usuario = Entry(root).grid(row=0, column=1)
text_senha = Entry(root).grid(row=1, column=1)

cmd_login = Button(root, width=10, text=' OK ').grid(row=2,column=1, sticky=E)

root.mainloop()