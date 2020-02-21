from tkinter import *

menu_incial = Tk()
menu_incial.title('app')
menu_incial.geometry('500x500')

texto = StringVar()
texto.set('hello world')

l1 = Label(
    menu_incial,
    font='Arial 20',
    bg='red',
    fg='white',
    textvariable=texto 
)
l1.pack()



menu_incial.mainloop()