from tkinter import *

root = Tk()

def print_rbt1():
    print('opção 1')
        
valorA = IntVar()

rbt1 = Radiobutton(root, text='opção A 1', variable=valorA, value=1, command=print_rbt1, indicatoron=0)
rbt2 = Radiobutton(root, text='opção A 2', variable=valorA, value=2)
rbt3 = Radiobutton(root, text='opção A 3', variable=valorA, value=3)

rbt1.pack()
rbt2.pack()
rbt3.pack()

rbt1.select() # p o radiobutão já ficar selecionado qnd iniciar

def ver_radio():
    print(valorA.get())

bt_exe = Button(root, text='Executar', command=ver_radio)
bt_exe.pack()

root.mainloop()