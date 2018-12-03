#TEMA:  Widget Grid

#Trabajando con grillas o tablas
####################################################################
from tkinter import *
####################################################################


####################################################################
raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Sticky alinea algo basandose en el sistemas cardinal (N, S, W, E) y puntos intermiedios
#Padx y Pady, me permite determinar una distancia entre un objeto y su entorno

nombre_label= Label(miFrame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)


apellido_label= Label(miFrame, text="Apellido:")
apellido_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

direccion_label= Label(miFrame, text="Direccion de casa:")
direccion_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)



cuadro_nombre = Entry(miFrame)
cuadro_nombre.grid(row=0, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="center")

cuadro_apellido = Entry(miFrame)
cuadro_apellido.grid(row=1, column=1, padx=10, pady=10)
cuadro_apellido.config(fg="red", justify="center")

cuadro_direccion = Entry(miFrame)
cuadro_direccion.grid(row=2, column=1, padx=10, pady=10)
cuadro_direccion.config(fg="red", justify="center")



#Hacemos un campo de contraseña
pass_label = Label(miFrame, text="Password: ")
pass_label.grid(row=3, column=0, padx=10, pady=10 )

cuadro_pass = Entry(miFrame)
cuadro_pass.grid(row=3, column=1, padx=10, pady=10 )
cuadro_pass.config(show="*")


raiz.mainloop()
####################################################################