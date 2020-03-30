# 037 - Python tkinter - SPINBOX

from tkinter import *

root = Tk()
root.geometry('300x300')

sb1 = Spinbox(root, from_=0, to=10)
sb1.pack()

sb2 = Spinbox(root, values=(2, 4, 8, 16, 32, 64), wrap=True) # p variar entre os valors
sb2.pack() # wrap é p qnd terminar apertando p cima, volte p o inicio

sb3 = Spinbox(root, values=('windows', 'linux', 'solaris'), wrap=True) # p variar entre os valors com string
sb3.pack()

def executar():
    print(sb2.get() + ' clicado')
    
bt = Button(root, text='clique', command=executar)
bt.pack()

root.mainloop()

