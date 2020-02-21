from tkinter import *


menu_inicial = Tk()
menu_inicial.title('App')


btn = Button(menu_inicial, text='executar')
btn.pack()

menu_inicial['bg']= 'blue' #bg=background

menu_inicial.geometry('400x200+100+100')
menu_inicial.mainloop()