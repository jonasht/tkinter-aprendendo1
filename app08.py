from tkinter import *

j = Tk()
j.title('App')
j.geometry('500x500')

l1 = Label(
    j,
    text='0123456789',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=4,
    anchor=CENTER # N, S, W, E, CENTER
).pack()

j.mainloop()


