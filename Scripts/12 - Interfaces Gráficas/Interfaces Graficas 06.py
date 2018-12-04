#TEMA - EJEMPLO - CALCULADORA

#columnspan --->Me permite determinar cuantas columnas ocupa una celda
#Solo suma :v
#################################################################
from tkinter import *
#################################################################


#################################################################
raiz = Tk()

mi_frame= Frame(raiz)
mi_frame.pack()

operacion = ""
resultado = 0

#--------------------Pantalla--------------------#
numero_pantalla = StringVar()

pantalla = Entry(mi_frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")



#--------------------Pulsaciones Teclado--------------------#
def numeroPulsado(num):
	global operacion

	if operacion != "":
		numero_pantalla.set(num)
		operacion=""
	else:		
		numero_pantalla.set(numero_pantalla.get() + num)


#--------------------Funcion Suma--------------------#
def suma(num):
	global operacion
	global resultado

	resultado+=int(num) 
	operacion="suma"

	numero_pantalla.set(resultado)

#--------------------Funcion elResultado--------------------#
def elResultado():
	global resultado
	numero_pantalla.set(resultado + int(numero_pantalla.get()))
	resultado=0

#--------------------Fila 1--------------------#
boton_7 = Button(mi_frame, text="7", width=3,  command=lambda:numeroPulsado("7"))
boton_7.grid(row=2, column=1)

boton_8 = Button(mi_frame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton_8.grid(row=2, column=2)

boton_9 = Button(mi_frame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton_9.grid(row=2, column=3)

boton_div = Button(mi_frame, text="/", width=3)
boton_div.grid(row=2, column=4)



#--------------------Fila 2--------------------#
boton_4 = Button(mi_frame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton_4.grid(row=3, column=1)

boton_5 = Button(mi_frame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton_5.grid(row=3, column=2)

boton_6 = Button(mi_frame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton_6.grid(row=3, column=3)

boton_mul = Button(mi_frame, text="X", width=3)
boton_mul.grid(row=3, column=4)



#--------------------Fila 3--------------------#
boton_1 = Button(mi_frame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton_1.grid(row=4, column=1)

boton_2 = Button(mi_frame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton_2.grid(row=4, column=2)

boton_3 = Button(mi_frame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton_3.grid(row=4, column=3)

boton_rest = Button(mi_frame, text="-", width=3)
boton_rest.grid(row=4, column=4)



#--------------------Fila 4--------------------#
boton_0 = Button(mi_frame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton_0.grid(row=5, column=1)

boton_coma = Button(mi_frame, text=",", width=3, command=lambda:numeroPulsado(","))
boton_coma.grid(row=5, column=2)

boton_igual = Button(mi_frame, text="=", width=3, command=lambda:elResultado())
boton_igual.grid(row=5, column=3)

boton_suma = Button(mi_frame, text="+", width=3, command=lambda:suma(numero_pantalla.get()))
boton_suma.grid(row=5, column=4)


raiz.mainloop()
#################################################################