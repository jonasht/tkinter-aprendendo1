from tkinter import *
import pylint

menu_incial = Tk()
menu_incial.title('app')
menu_incial.geometry('500x300')
def cmd_click(msm):
    print(msm)
    #botao
cmd1 = Button(menu_incial, text='Executar', command=lambda: cmd_click('nova mensagem'))
cmd1.pack()

cmd2 = Button(menu_incial, text='outro Executar', command=lambda: print('ok'))
cmd2.pack()

menu_incial.mainloop() 