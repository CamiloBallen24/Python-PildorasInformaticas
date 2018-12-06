#Practica guiada
##########################################################################################################################
from tkinter import *
from tkinter import messagebox
import sqlite3
##########################################################################################################################

##########################################################################################################################
root=Tk()

#--------------------BARRA DE MENU--------------------#
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar")
bbdd_menu.add_command(label="Salir")

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar Campos")


crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de..")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

#--------------------COMIENZO DE CAMPOS--------------------#
mi_frame_01=Frame(root)
mi_frame_01.pack()



root.mainloop()
##########################################################################################################################