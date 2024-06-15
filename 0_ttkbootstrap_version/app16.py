from tkinter import *
from ttkbootstrap import Window as Tk, Label, Button, Entry
#-----------------------------------------------------------
# funcao
def mostrarNome():
    vartexto.set('oi ' + text1.get())
    
    
#-----------------------------------------------------------
# GUI
root = Tk()
root.title('Aplicação')

vartexto = StringVar()

#-----------------------------------------------------------
# widgets
l1 = Label(root, text='qual seu nome:')
text1 = Entry(root)
botao = Button(root, text='Executar', command=mostrarNome)
l2 = Label(root, textvariable = vartexto)

#-----------------------------------------------------------
#layout
l1.grid()
text1.grid()
botao.grid()
l2.grid()


root.mainloop()