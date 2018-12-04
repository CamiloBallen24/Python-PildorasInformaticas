#TEMA: INTERFACES GRAFICAS

#Una interfaz grafica, esta compuesta por una raiz(Ventana)
#Esta raiz contiene uno o varios frames y estos contienen Widgets
#En realidad para python un todo es un widget, pero es 
#mejor manejarlo de la anterior manera

##############################################################################################################################################################################
#Libreria que me ayudara a realizar las interfaces
from tkinter import *
##############################################################################################################################################################################

##############################################################################################################################################################################
#Creo la raiz
raiz=Tk()

#Dotamos de titulo a la ventana
raiz.title("Primera Ventana")

#Redimensionar (width, height) 
#0->No redimencionar
#1->Redimencionar
#Por Defecto se puede redimensionar
raiz.resizable(1, 1)

#Icono de la ventana
raiz.iconbitmap("Imagenes\cat.ico")

#dimesiones de la ventana
#Si no ponemos tamaño la raiz se ajustara al tamaño del frame
#raiz.geometry("600x300")


#Color de fondo
raiz.config(bg="RED")

##############################################################################################################################################################################


##############################################################################################################################################################################
#Creamos un Frame
miFrame=Frame()



#Empaqueto el frame
#Podemos definir algunas propiedades del 
#frame antes de empaquetarlo
#ver documentacion -> https://docs.python.org/3/library/tkinter.html#packer-options

#miFrame.pack(side="right") #-> El Frame se anclara a la derecha

#Anchor se maneja en puntor cardinales
#miFrame.pack(side="left", anchor="n") #-> El Frame se anclara a la parte superior izquierda

#miFrame.pack(fill="x") #-> Cuando se aumente en tamaño de la raiz el frame se expandira horizontalmente

#miFrame.pack(fill="y", expand="True") #-> Cuando se aumente en tamaño de la raiz el frame se expandira verticalmente

#miFrame.pack(fill="both") #-> Cuando se aumente en tamaño de la raiz el frame se expandira en el eje x y el eje y 

miFrame.pack()



#Cambio de color fondo del frame
miFrame.config(bg="GREEN")



#Cambiar el borde
miFrame.config(bd=35) #tamaño
#miFrame.config(relief="groove") #boder tipo 01
miFrame.config(relief="sunken") #boder tipo 02


#Icono del mouse en el frame
miFrame.config(cursor="pirate")


#Tamaño del frame
#El tamaño del frame es fijo por defecto -> es decir no se redimensiona
miFrame.config(width="500", height="300")

##############################################################################################################################################################################



##############################################################################################################################################################################
#Muestro la raiz con un bucle infinito
raiz.mainloop()
##############################################################################################################################################################################



##############################################################################################################################################################################
#Si tenemos un archivo .py y cambiamos su extesion a .pyw
#Quedara como un ejecutable
##############################################################################################################################################################################