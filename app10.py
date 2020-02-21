from tkinter import *

menu_incial = Tk()
menu_incial.title('app')
menu_incial.geometry('500x500')



lb2 = Label(menu_incial)
lb2['text']='frase de lb2'
lb2['font']='Arial 20'
lb2['bd']=1
lb2['relief']='solid'
lb2.pack()

print(lb2.keys())

for itens in lb2.keys():
    print(itens, ' : ', lb2[itens])
    #print(f'{itens} : {lb2[itens]}')
    
#lb2['text']='novo texto' pode definir essas coisas de novo depois dela ter sido ja definida

#print(lb1['font'])

menu_incial.mainloop()