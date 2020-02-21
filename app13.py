from tkinter import *

root = Tk()

root.title('log in')

Label(root, text=' texto ', bg='yellow').grid(column=0)
Label(root, text=' texto ', bg='purple').grid(column=1)
Label(root, text=' texto ', bg='green').grid(columnspan=3, sticky='we')
Label(root, text=' texto ', bg='purple').grid(column=2)



root.mainloop()