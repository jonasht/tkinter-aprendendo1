from tkinter import *
# --- GUI --- ------------------------------------
root = Tk()
root.title('app')

# --- widgets --- ---------------------------------
frame_nome = Frame(root)
frame_moradia = Frame(root)

label_nome = Label(frame_nome, text='nome:')
label_apelido  = Label(frame_nome, text='apelido:')
label_rua = Label(frame_moradia, text='rua:')
label_cidade = Label(frame_moradia, text='cidade:')

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_moradia)
text_cidade = Entry(frame_moradia)

cmd_salvar = Button(root, text='salvar')
#- layout ----------------------------------------

label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
text_nome.grid(row=0, column=1)
text_apelido.grid(row=1, column=1)

label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

frame_nome.grid(row=0, column=0)
frame_moradia.grid(row=0, column=1)

cmd_salvar.grid(column=1)


root.mainloop()