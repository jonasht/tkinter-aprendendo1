from tkinter import *

menu_inicial = Tk()
menu_inicial.title('app')
menu_inicial['bg']=('orange red')

l1abel = Label(menu_inicial, 
        text='it is a Label 1 here',
        bg='red',
        font='Arial 20',
        width=20
        ).pack()

menu_inicial.geometry('500x500')

menu_inicial.mainloop()