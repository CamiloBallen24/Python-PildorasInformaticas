#TEMA: INTERFACES GRAFICAS


##########################################################
#Libreria que me ayudara a realizar las interfaces
from tkinter import *
##########################################################

##########################################################
#Creo la raiz
raiz=Tk()

#Dotamos de titulo a la ventana
raiz.title("Primera Ventana")

#Redimensionar (width, height) 
#0->No redimencionar
#1->Redimencionar
raiz.resizable(1, 1)

#Icono de la ventana
raiz.iconbitmap("Imagenes\cat.ico")

#dimesiones de la ventana
raiz.geometry("600x300")

#Color de fondo
raiz.config(bg="RED")

#La muestro con un bucle infinito
raiz.mainloop()
##########################################################
