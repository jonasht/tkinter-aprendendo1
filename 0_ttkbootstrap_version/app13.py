from ttkbootstrap import Window as Tk, Label
root = Tk()

root.title('log in')

Label(root, text=' texto ', background='yellow').grid(column=0)
Label(root, text=' texto ', background='purple').grid(column=1)
Label(root, text=' texto ', background='green').grid(columnspan=3, sticky='we')
Label(root, text=' texto ', background='purple').grid(column=2)



root.mainloop()