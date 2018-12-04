#TEMAS: VENTANAS EMERGENTES PARA ABRIR ARCHIVOS
######################################################################
from tkinter import *
from tkinter import filedialog
######################################################################

######################################################################
def abreFichero():
	ficheros_abrir=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"), ("Todos los Ficheos", "*.*"))
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=ficheros_abrir)
	print(fichero)
######################################################################


######################################################################
root=Tk()

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
######################################################################
	
