#TEMA: Radio Button


################################################################
from tkinter import *
################################################################ACTIVE



################################################################
def imprimir():
	#print(var_opcion.get())
	if var_opcion.get() == 1:
		etiqueta.config(text="Has elegido Masculino.")
	elif var_opcion.get() == 2:		
		etiqueta.config(text="Has elegido Femenino.")
	else:
		etiqueta.config(text="Has elegido Otros.")
################################################################



################################################################
root=Tk()

var_opcion= IntVar()

Label(root, text="Genero:" ).pack()

Radiobutton(root, text="Masculino", variable=var_opcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=var_opcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otros", variable=var_opcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
################################################################