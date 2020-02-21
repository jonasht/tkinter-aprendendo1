from tkinter import *

menu_incial = Tk()
menu_incial.title('configurações para a tela ficar no meio')


#dimisões da janela
largura = 500
altura = 300

#resolução do sistema
largura_screen = menu_incial.winfo_screenwidth()
altura_screen = menu_incial.winfo_screenheight()

#posição da janela
posX = largura_screen/2 - largura/2
posY = altura_screen/2 - altura/2

#definir a geometry
menu_incial.geometry('%dx%d+%d+%d' % (largura, altura, posX, posY))

menu_incial = Label(menu_incial, text='helloWorld/oi mundo').grid(row=0, column=0)

menu_incial.mainloop()