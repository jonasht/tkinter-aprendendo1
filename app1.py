from tkinter import *

menu_incial = Tk()
menu_incial.title('PrimeiroApp')
#lb = Label(menu_incial, text='algoaqui')
#lb.grid(row=0, column=0)
print('working')
menu_incial.geometry('500x250+400+200')# icon da janela com o endereço da pasta

menu_incial.iconbitmap('images\icon.ico')

#menu_incial.resizable(True, True)# True, True/ False,False ou 0,0/1,1 serve para puxar a janela com mouse
#menu_incial.minsize(width = 500, height = 250)
#menu_incial.maxsize(700, 400)
#menu_incial.state('iconic')# zoomed para quando iniciar a janela, maximinzando a tela/TelaInteira //  iconic para a janela aparecer minimizada 

menu_incial.mainloop()
