from tkinter import *

root = Tk()
root.geometry('+600+200')
root.title('listbox')

lista = Listbox(root)
lista.pack()

#inserir um item de cada vez
lista.insert(END, 'primeira palavra da lista')
lista.insert(1, 'segunda palavra da lista')
lista.insert(END, 'terceira palavra da lista')
lista.insert(END, 'quarta palavra da lista')



root.mainloop()