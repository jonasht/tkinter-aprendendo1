from ttkbootstrap import Window as Tk, Label, Entry, Frame
from ttkbootstrap.constants import *

#--------------------------------------------------
# meu widget
class FrameNome(Frame):
    def __init__(self, a):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['border'] = 2
        self['relief'] = SOLID
    
        label_nome = Label(self, text='Nome:')
        text_nome = Entry(self)
        label_nome.grid(row=0, column = 0)
        text_nome.grid(row=0, column=1)
    
#--------------------------------------------------
# GUI
root = Tk()
root.title('app')

frame_nome_1 = FrameNome(root).grid()
frame_nome_2 = FrameNome(root).grid()
frame_nome_3 = FrameNome(root).grid()
frame_nome_4 = FrameNome(root).grid()


root.mainloop()