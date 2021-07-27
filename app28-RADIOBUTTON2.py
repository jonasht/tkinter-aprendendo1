from tkinter import *

root = Tk()

frameA = Frame(root)
frameA.pack()

frameB = Frame(root)
frameB.pack()

def print_rbt1():
    print('opção 1')
        
valorA = IntVar()
valorB = IntVar()

rbtA1 = Radiobutton(frameA, text='opção A 1', value=1, command=print_rbt1, indicatoron=0)
rbtA2 = Radiobutton(frameA, text='opção A 2', variable=valorA, value=2)
rbtA3 = Radiobutton(frameA, text='opção A 3', variable=valorA, value=3)

rbtA1.pack()
rbtA2.pack()
rbtA3.pack()

rbtB1 = Radiobutton(frameB, text='opção A 1', variable=valorB, value=1)
rbtB2 = Radiobutton(frameB, text='opção A 2', variable=valorB, value=2)
rbtB3 = Radiobutton(frameB, text='opção A 3', variable=valorB, value=3)

rbtB1.pack()
rbtB2.pack()
rbtB3.pack()

rbtA1.select() # p o radiobutão já ficar selecionado qnd iniciar

def ver_radio():
    print(valorA.get())

bt_exe = Button(root, text='Executar', command=ver_radio)
bt_exe.pack()

root.mainloop()