from tkinter import *



root = Tk()
root.geometry('500x200+600+200')
root.title('scale')

slide = Scale(root, from_=0, to=100)
slide.pack()

def Valor():
    print(slide1.get())

slide1 = Scale(root,
             from_=0,
             to=100,
             orient=HORIZONTAL,
             resolution=0.5,
             )

slide1.pack()

cmd = Button(root, text='ver valor', command=Valor)
cmd.pack()
root.mainloop()