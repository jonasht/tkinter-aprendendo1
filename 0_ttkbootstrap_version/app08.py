from tkinter import *
import ttkbootstrap as ttk
j = ttk.Window()

j.title('App')
j.geometry('500x500')

Label(
    j,
    text='0123456789',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=4,
    anchor=CENTER # N, S, W, E, CENTER
).pack()
ttk.Label(
    j,
    text='0123456789',
    font='Arial 20',
    border=1,
    relief='solid',
    width=25,
    
    anchor=CENTER # N, S, W, E, CENTER
).pack(ipady=40)
j.mainloop()


