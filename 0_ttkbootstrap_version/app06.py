import ttkbootstrap as ttk

menu_inicial = ttk.Window()
menu_inicial.title('app6')
menu_inicial['bg']=('orange red')

l1abel = ttk.Label(menu_inicial, 
        text='it is a Label 1 here',
        background='red',
        font='Arial 20',
        width=20
        ).pack()

menu_inicial.geometry('500x500')

menu_inicial.mainloop()