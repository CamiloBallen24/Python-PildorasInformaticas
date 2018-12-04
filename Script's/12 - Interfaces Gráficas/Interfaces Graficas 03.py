#TEMA:  Widget Entry

#Es un cuadro de texto en el que se puede escribit un texto.

####################################################################
from tkinter import *
####################################################################


####################################################################
raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Creando cuadro de texto
cuadroTexto = Entry(miFrame)
cuadroTexto.place(x=100, y=100)

raiz.mainloop()
####################################################################