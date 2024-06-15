from ttkbootstrap import Window as Tk
from ttkbootstrap import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self.config(bootstyle=SUCCESS,)
        self['border']=2
        self['relief'] = SOLID
        
        self.text1_text = StringVar()
        self.label1_text = StringVar()
        
        # --- widgets ---
        self.label1 = Label(self, background='sea green', textvariable = self.label1_text).grid()
        text1 = Entry(self, textvariable = self.text1_text).grid()
        style = Style()
        style.configure('TButton', background='dark sea green')
        cmd1 = Button(self, text='clique', command = self.Executar).grid()
    def Executar(self):
        self.label1_text.set(f'oi, {self.text1_text.get()}.')
        
root = Tk()
root.title('app')

#root.geometry('300x200')

frm1 = MinhaFrame(root).grid(row=1)
frm2 = MinhaFrame(root).grid(row=2)
frm3 = MinhaFrame(root).grid(row=3)

frm1 = MinhaFrame(root).grid(row=1, column=1)
frm2 = MinhaFrame(root).grid(row=2, column=1)
frm3 = MinhaFrame(root).grid(row=3, column=1)

root.mainloop()