#TEMA:  Widget Grid

#Trabajando con grillas o tablas
####################################################################
from tkinter import *
####################################################################


####################################################################
def codigoBoton():
	mi_nombre.set("Camilo")
####################################################################


####################################################################
raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Variable que usaremos en el codigo :v
mi_nombre= StringVar()


#Sticky alinea algo basandose en el sistemas cardinal (N, S, W, E) y puntos intermiedios
#Padx y Pady, me permite determinar una distancia entre un objeto y su entorno

#Creamos algunos label y unos cuadros de textos
nombre_label= Label(miFrame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)


apellido_label= Label(miFrame, text="Apellido:")
apellido_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

direccion_label= Label(miFrame, text="Direccion:")
direccion_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)


#Le asociamos al cuadro de texto la variable mi_nombre
cuadro_nombre = Entry(miFrame, textvariable=mi_nombre)
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



#Texto largo o Caja de Texto
comentarios_label= Label(miFrame, text="Comentarios: ")
comentarios_label.grid(row=4, column=0, padx=10, pady=10)

texto_comentarios= Text(miFrame, width=16, height=5)
texto_comentarios.grid(row=4, column=1, padx=10, pady=10)


#Creamos un scroll bar y se lo asignamos a la caja de texto
#stick="nswe" nos permite desplazarla el scroll bar
scroll_vertical= Scrollbar(miFrame, command=texto_comentarios.yview)
scroll_vertical.grid(row=4, column=2, padx=10, pady=10, sticky="nswe")


#nos permite que sea dinamico (dependiendo la posicion en el texto, se mueva)
texto_comentarios.config(yscrollcommand=scroll_vertical.set)


#Boton
#Cuando se oprima el boton se ejecutara la funcion codigo Boton
boton_envio= Button(raiz, text="Enviar", command=codigoBoton)
boton_envio.pack()



raiz.mainloop()
####################################################################


