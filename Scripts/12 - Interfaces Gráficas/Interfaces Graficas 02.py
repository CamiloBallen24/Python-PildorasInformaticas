#TEMA: LABEL

#Un label es una zona en la que puedo mostrar texto o imagenes
######################################################################
from tkinter import *
######################################################################import


######################################################################
root = Tk();

miFrame=Frame(root, width=700, height=800)

miFrame.pack()

#Creamos un label
miLabel = Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18))

#Agregamos el label, respetando las dimensiones y en una posicion especifica
miLabel.place(x=50, y=50)

#Label con imagen
miImagen = PhotoImage(file="Imagenes\messi.png")

#Forma reducidad de label
Label(miFrame, image=miImagen).place(x=0, y=100)


root.mainloop()
######################################################################