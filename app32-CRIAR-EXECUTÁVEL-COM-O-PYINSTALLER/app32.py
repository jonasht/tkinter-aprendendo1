# CRIAR-EXECUTÁVEL-COM-O-PYINSTALLER

from tkinter import *

root = Tk()
root.geometry('300x300+550+200')
root.title('App')



def Abrir_formulario():
    # top level
    top = Toplevel()

    top.title('novo formulario')
    top.geometry('200x100')

    lb1 = Label(top, text='label na nova janela')
    lb1.pack()
    
bt = Button(root, text='abrir formulario', command=Abrir_formulario)
bt.pack()




root.mainloop()