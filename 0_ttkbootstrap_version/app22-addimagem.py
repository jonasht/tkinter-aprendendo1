from ttkbootstrap import *


root = Window()

img = PhotoImage(file='images/brain2.png')
lb = Label(root, text='Brain', font='Arial 20 bold').pack()
label_imagem = Label(root, image=img).pack()

root.mainloop()