from tkinter import *
from ttkbootstrap import Window
j = Window()
# ttkbootstrap não funciona os relief *** ***
j.title('App')
j['bg']='orange red'
j.bind('q', lambda x: j.quit())
width = j.winfo_screenwidth()
height = j.winfo_screenheight()
j.geometry(f'{width}x{height}')

border = 50
Label(
    j,
    text='solid',
    font='Arial 20',
    bd=border,
    relief='solid'
).pack(anchor=NW)
Label(
    j,
    text='flat',
    font='Arial 20',
    bd=border,
    relief='flat'
).pack(anchor=N)
Label(
    j,
    text='raised',
    font='Arial 20',
    bd=border,
    relief='raised'
).pack(side=TOP, anchor=NE)

Label(
    j,
    text='sunken',
    font='Arial 20',
    bd=border,
    relief='sunken'
).pack(side=BOTTOM, anchor=SW)

Label(
    j,
    text='ridge',
    font='Arial 20',
    bd=border,
    relief='ridge'
).pack(side=RIGHT)

Label(
    j,
    text='groove',
    font='Arial 20',
    bd=border,
    relief='groove'
).pack(side=RIGHT)

j.mainloop()