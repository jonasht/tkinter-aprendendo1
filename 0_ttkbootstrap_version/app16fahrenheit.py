from ttkbootstrap import Window as Tk, StringVar, Label, Entry, Button
from ttkbootstrap.constants import *

#-----------------------------------------------------------
# funcao
def calcular():
    f = float(text.get())
    c = (f - 32) * 5/9
    final.set(str(round(c, 1)) + ' graus celsius')
#-----------------------------------------------------------
# GUI
root = Tk()
root.title('fahrenheit')
root.geometry('+600+300')
root['bg']='dark sea green'
final = StringVar()

#-----------------------------------------------------------
# widgets

label1 = Label(root, text='graus fahrenheit:', foreground='black', background='dark sea green', font='Arial 15')
text = Entry(root)
butao = Button(root, text='Calcular', bootstyle=SUCCESS, command = calcular)
label_resultado = Label(root, background='dark sea green', textvariable = final)

#-----------------------------------------------------------
#layout

label1.grid()
text.grid()
butao.grid()
label_resultado.grid()

root.mainloop()