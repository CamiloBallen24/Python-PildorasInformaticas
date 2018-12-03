#TEMA: Text y Button

#Text: Introducir textos largo
#Button: Botones toda la vida

####################################################################
from tkinter import *
####################################################################

####################################################################
def codigoBoton():
	print("Boton Oprimido")
####################################################################


####################################################################
raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()


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