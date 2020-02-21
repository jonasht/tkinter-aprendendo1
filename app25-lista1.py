from tkinter import *

root = Tk()
root.title('listbox')

root.geometry('+600+200')
lista = Listbox(root, selectmode=EXTENDED)#selectmode=EXTENDED - p conseguir selecionr varios itens
lista.pack()


#inserir um item de cada vez
nomes =['jonas', 'lucas', 'carlos', 'pedro']
for nome in nomes:
    lista.insert(END, nome)
#lista.delete(1, END)
def Executar():
    print(lista.get(ACTIVE))
    
cmd = Button(root, text=' ok ', width=10, command=Executar).pack()


root.mainloop()