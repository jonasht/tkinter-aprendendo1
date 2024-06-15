import ttkbootstrap as ttk

menu_incial = ttk.Window()
menu_incial.title('app')
menu_incial.geometry('500x500')

texto = ttk.StringVar()
texto.set('hello world')

l1 = ttk.Label(
    menu_incial,
    font='Arial 20',
    background='red',
    foreground='white',
    textvariable=texto 
)
l1.pack()



menu_incial.mainloop()