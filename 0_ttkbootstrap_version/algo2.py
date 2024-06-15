from tkinter import *

# using grid
# +------+-------------+
# | btn1 |    btn2     |
# +------+------+------+
# | btn3 | btn3 | btn4 |
# +-------------+------+
root = Tk()

btn1 = Button(root, text='btn1')
btn2 = Button(root,text='btn2')
btn3 = Button(root,text='btn3')
btn4 = Button(root,text='btn4')
btn5 = Button(root,text='btn5')

btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')

root.mainloop()