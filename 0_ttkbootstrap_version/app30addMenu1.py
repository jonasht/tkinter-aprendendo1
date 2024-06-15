# 038 - Python tkinter - ADICIONAR MENUS À APLICAÇÃO
# from tkinter import *
from ttkbootstrap import *

root = Window()
root.geometry('300x300')
root.style.theme_use('darkly')

meuMenu = Menu(root )

def novoArq_click():
    print('novo arquivo')
    
#   menu file
fileMenu = Menu(meuMenu, tearoff=0) 
fileMenu.add_command(label='Novo', command=novoArq_click) # o label tem escrever com letra minuscula 'l'abel e não 'L'abel
fileMenu.add_command(label='abrir')
fileMenu.add_command(label='salvar')
fileMenu.add_separator()
fileMenu.add_command(label='sair', command=root.quit)
meuMenu.add_cascade(label='file', menu=fileMenu)

# menu edit
fileEdit = Menu(meuMenu, tearoff=0) 
fileEdit.add_command(label='Copiar') # o label tem escrever com letra minuscula 'l'abel e não 'L'abel
fileEdit.add_command(label='Colar')
fileEdit.add_command(label='SelecionarTudo')
meuMenu.add_cascade(label='Edit', menu=fileMenu)



root.config(menu = meuMenu)

root.mainloop()