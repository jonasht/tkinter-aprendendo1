from ttkbootstrap import Window as Tk, Label, Button, Entry
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

menu_incial = Tk()

menu_incial.title('algo')
# menu_incial['bg']='black'

lb1 = Label(menu_incial,
 text='este é o Label 1',
 font='Arial 20 bold italic',
 foreground='green', background='black')

lb2 = Label(menu_incial,
 text='este é o Label 2', 
 foreground='red')

lb3 = Label(menu_incial,
 text='este é o Label 3', 
 background='black', foreground='#aaaaaa',
 font='Verdana 42 bold').pack()

style = ttk.Style()
style.configure('TButton', font='Arial 23 bold')
cmd = Button(menu_incial, text='executar', bootstyle=SUCCESS)
entrada =  Entry(menu_incial, background='white', foreground='lightgray')
entrada.insert(0, 'entrada')

# pack
lb2.pack()
lb1.pack()
entrada.pack()
cmd.pack()

menu_incial.geometry('600x400')
menu_incial.mainloop()

