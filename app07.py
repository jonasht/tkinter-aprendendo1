from tkinter import *
j = Tk()
j.title('App')
#j['bg']='red'

border = 50
l1 = Label(
    j,
    text='solid',
    font='Arial 20',
    bd=border,
    relief='solid'
).pack()
l1 = Label(
    j,
    text='flat',
    font='Arial 20',
    bd=border,
    relief='flat'
).pack()
l1 = Label(
    j,
    text='raised',
    font='Arial 20',
    bd=border,
    relief='raised'
).pack()

l1 = Label(
    j,
    text='sunken',
    font='Arial 20',
    bd=border,
    relief='sunken'
).pack()

l1 = Label(
    j,
    text='ridge',
    font='Arial 20',
    bd=border,
    relief='ridge'
).pack()

l1 = Label(
    j,
    text='groove',
    font='Arial 20',
    bd=border,
    relief='groove'
).pack()

j.geometry('500x500')
j.mainloop()