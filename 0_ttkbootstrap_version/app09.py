from tkinter import *
import ttkbootstrap as ttk
j = Tk()
j.geometry('500x500')
j.title('App')

Label(
    j,
    text='frase de testes\n teste',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=30,
    height=5,
    
    
).pack()

ttk.Label(
    j,
    text='frase de testes\n teste',
    font='Arial 20',
    border=1,
    relief='solid',
    width=30,
    
    
    
).pack()



j.mainloop()