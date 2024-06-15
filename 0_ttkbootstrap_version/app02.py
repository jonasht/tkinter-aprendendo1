import ttkbootstrap as ttk


menu_inicial = ttk.Window()

menu_inicial.title('App')


btn = ttk.Button(menu_inicial, text='executar')
btn.pack()

menu_inicial['bg']= 'blue'

menu_inicial.geometry('400x200+100+100')
menu_inicial.mainloop()