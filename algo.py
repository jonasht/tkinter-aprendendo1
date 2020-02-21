# Python program to create a simple janela 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

# globally declare the expressao variable 
expressao = '' 


# Function to update expressiom 
# in the text entry box 
def press(num): 
	# point out the global expressao variable 
	global expressao 

	# concatenation of string 
	expressao = expressao + str(num) 

	# update the expressao by using set method 
	equacao.set(expressao) 


# Function to evaluate the final expressao 
def igualbt(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expressao 

		# eval function evaluate the expressao 
		# and str function convert the result 
		# into string 
		total = str(eval(expressao)) 

		equacao.set(total) 

		# initialze the expressao variable 
		# by empty string 
		expressao = '' 

	# if error is generate then handle 
	# by the except block 
	except: 

		equacao.set(' digito invalido ') 
		expressao = '' 


# Function to limpar the contents 
# of text entry box 
def limpar(): 
	global expressao 
	expressao = '' 
	equacao.set('') 


# Driver code 
if __name__ == '__main__': 
	# create a janela window 
	janela = Tk() 

	# set the background colour of janela window 
	janela.configure(background='light green') 

	# set the title of janela window 
	janela.title('Calculadora') 

	# set the configuration of janela window 
	janela.geometry('365x225') 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equacao = StringVar() 

	# create the text entry box for 
	# showing the expressao . 
	expressao_campo = Entry(janela, textvariable=equacao) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expressao_campo.grid(columnspan=4, ipadx=70) 

 

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(janela, text=' 1 ', fg='black', bg='dark green', 
					command=lambda: press(1), height=2, width=7) 
	button1.grid(row=3, column=0) 

	button2 = Button(janela, text=' 2 ', fg='black', bg='dark green', 
					command=lambda: press(2), height=2, width=7) 
	button2.grid(row=3, column=1) 

	button3 = Button(janela, text=' 3 ', fg='black', bg='dark green', 
					command=lambda: press(3), height=2, width=7) 
	button3.grid(row=3, column=2) 

	button4 = Button(janela, text=' 4 ', fg='black', bg='dark green', 
					command=lambda: press(4), height=2, width=7) 
	button4.grid(row=2, column=0) 

	button5 = Button(janela, text=' 5 ', fg='black', bg='dark green', 
					command=lambda: press(5), height=2, width=7) 
	button5.grid(row=2, column=1) 

	button6 = Button(janela, text=' 6 ', fg='black', bg='dark green', 
					command=lambda: press(6), height=2, width=7) 
	button6.grid(row=2, column=2) 

	button7 = Button(janela, text=' 7 ', fg='black', bg='dark green', 
					command=lambda: press(7), height=2, width=7) 
	button7.grid(row=1, column=0) 

	button8 = Button(janela, text=' 8 ', fg='black', bg='dark green', 
					command=lambda: press(8), height=2, width=7) 
	button8.grid(row=1, column=1) 

	button9 = Button(janela, text=' 9 ', fg='black', bg='dark green', 
					command=lambda: press(9), height=2, width=7) 
	button9.grid(row=1, column=2) 

	button0 = Button(janela, text=' 0 ', fg='black', bg='dark green', 
					command=lambda: press(0), height=2, width=7) 
	button0.grid(row=4, column=0) 

	plus = Button(janela, text=' + ', fg='black', bg='dark green', 
				command=lambda: press('+'), height=2, width=7) 
	plus.grid(row=1, column=3) 

	menus = Button(janela, text=' - ', fg='black', bg='dark green', 
				command=lambda: press('-'), height=1, width=7) 
	menus.grid(row=3, column=3) 

	multiplicar = Button(janela, text=' * ', fg='black', bg='dark green', 
					command=lambda: press('*'), height=1, width=7) 
	multiplicar.grid(row=4, column=3) 

	dividir = Button(janela, text=' / ', fg='black', bg='dark green', 
					command=lambda: press('/'), height=1, width=7) 
	dividir.grid(row=5, column=3) 

	igual = Button(janela, text=' = ', fg='black', bg='dark green', 
				command=igualbt, height=1, width=7) 
	igual.grid(row=5, column=2) 

	limpar = Button(janela, text='limpar', fg='black', bg='dark green', 
				command=limpar, height=1, width=7) 
	limpar.grid(row=5, column='1') 

	# start the janela 
	janela.mainloop() 
