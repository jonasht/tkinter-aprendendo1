from ttkbootstrap import Window as Tk, Entry, Label, Button
#------------------------------------------------------------
# funcoes
def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()
    
#------------------------------------------------------------
# GUI
root = Tk()
root.title('App')
root['bg']='lightgreen'
#------------------------------------------------------------
# Widgets
t1=Entry(root)
t2=Entry(root)
t3=Entry(root)

l1=Label(root, background='lightgreen')
l2=Label(root, background='lightgreen')
l3=Label(root, background='lightgreen')

b=Button(root, text='executar', command=executar)
#------------------------------------------------------------
# Layout
t1.grid()
t2.grid()
t3.grid()

l1.grid()
l2.grid()
l3.grid()

b.grid()

t1.focus()


root.mainloop()


