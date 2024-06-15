from tkinter import *
import ttkbootstrap as ttk

#

class minhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bg']='red'
        
# print(help(Frame))

class minhaFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self['bg']='red'
        
print(help(Frame))