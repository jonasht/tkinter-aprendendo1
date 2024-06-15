from tkinter import *
import ttkbootstrap as ttk


root = ttk.Window()
root.place_window_center()
root.style.theme_use('darkly')

root.geometry('500x200')
root.title('scale')

slide1 = ttk.Scale(root, from_=0, to=100, orient=VERTICAL)
slide1.pack()

def Valor():
    print(slide1.get())

slide2 = Scale(root,
             from_=0,
             to=100,
             orient=HORIZONTAL,
             resolution=0.5,
             )

slide2.pack()

cmd = Button(root, text='ver valor', command=Valor)
cmd.pack()
root.mainloop()