from tkinter import *
import ttkbootstrap as ttk
menu_incial = ttk.Window()

menu_incial.title('app')
menu_incial.geometry('500x500')

menu_incial.bind('q', lambda x: menu_incial.quit())


lb2 = ttk.Label(menu_incial)
lb2['text']='frase de lb2'
lb2['font']='Arial 20'
lb2['border']=1
lb2['relief']='solid'
lb2.pack()

# print(lb2.keys())
print('label2 keys:')
for itens in lb2.keys():
    print(itens, ' : ', lb2[itens])

menu_incial.mainloop()