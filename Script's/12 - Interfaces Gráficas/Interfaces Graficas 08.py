#TEMA: Check Button

#Casillas de verificacion

################################################################################
from tkinter import *
################################################################################

################################################################################
def opcionesViaje():
	opcion_escogida = ""
	if(playa.get() == 1):
		opcion_escogida += "   playa"

	if(montana.get() == 1):
		opcion_escogida += "    montana"

	if(turismo_rural.get() == 1):
		opcion_escogida += "   Turismo Rural"

	texto_final.config(text=opcion_escogida)
################################################################################



################################################################################
root= Tk()

root.title("Ejemplo - CheckButton")

foto=PhotoImage(file="Imagenes\emoji.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()


playa=IntVar()
montana=IntVar()
turismo_rural=IntVar()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",  variable=montana, onvalue=1, offvalue=0, command=opcionesViaje ).pack()
Checkbutton(frame, text="Turismo Rural",  variable=turismo_rural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

texto_final = Label(frame)
texto_final.pack()


root.mainloop()
################################################################################