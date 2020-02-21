from tkinter import *

def mostrarNome():
    nome = textEntrad.get()
    label_final = Label(root, bg='dark sea green', text='teu nome é ' + nome)
    label_final.grid()
    label_finalen = Label(root, bg='dark sea green', text='your name is ' + nome)
    label_finalen.grid()    
    
    
root = Tk()
root.title()
root.geometry('230x250')
root['bg']='dark sea green'

l1 = Label(root, text='Qual teu nome: ', bg='dark sea green', font='Arial 18 bold')
lb1en = Label(root, text='What is your name: ', bg='dark sea green', font='Arial 18 bold')
textEntrad = Entry(root)
botao1 = Button(root, text='executar', bg='dark green', font='Arial 12 bold', command=mostrarNome)

l1.grid()
lb1en.grid()
textEntrad.grid()
botao1.grid()

root.mainloop()