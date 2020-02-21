from tkinter import *
menu_incial = Tk()

menu_incial.title('algo')
menu_incial['bg']='black'

lb1 = Label(menu_incial,
 text='este é o Label 1',
 font='Arial 20 bold italic',
 fg='green', bg='black')

lb2 = Label(menu_incial,
 text='este é o Label 2', 
 bg='black', fg='red')

lb3 = Label(menu_incial,
 text='este é o Label 3', 
 bg='black', fg='#aaaaaa',
 font='Verdana 42 bold').pack()


cmd = Button(menu_incial, text='executar', bg='green', fg='yellow', font='Arial 23 bold')
entrada =  Entry(menu_incial, text='algo', bg='white')
# pack
lb2.pack()
lb1.pack()
entrada.pack()
cmd.pack()

menu_incial.geometry('600x400')
menu_incial.mainloop()

