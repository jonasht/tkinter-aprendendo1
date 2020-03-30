from tkinter import *

root = Tk()
Button(root, text='NOUN').pack(side=RIGHT, anchor=NE)
Button(root, text='Top').pack(side=TOP,  fill=X, expand=YES)
Button(root, text='Center').pack(fill=X, anchor=W, expand=YES)

Button(root, text='Left').pack(side=LEFT, fill=X, expand=YES)
Button(root, text='Center').pack(side=LEFT, fill=X, expand=YES)
Button(root, text='Right').pack(side=LEFT, fill=X, expand=YES)       

        
root.mainloop()