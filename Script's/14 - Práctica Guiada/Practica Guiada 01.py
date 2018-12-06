#Practica guiada
##########################################################################################################################
from tkinter import *
from tkinter import messagebox
import sqlite3
##########################################################################################################################






##########################################################################################################################
#Funciones

def conexionBBDD():
	mi_conexion=sqlite3.connect("Usuarios")

	mi_cursor=mi_conexion.cursor()

	try:
		mi_cursor.execute('''
			CREATE TABLE DATOS_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD Creada con éxito")

	except:
		messagebox.showwarning("BBDD", "¡Atencion!, la BBDD ya existe")



def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

	if valor == "yes":
		root.destroy()
##########################################################################################################################






##########################################################################################################################
root=Tk()

#--------------------BARRA DE MENU--------------------#
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexionBBDD)
bbdd_menu.add_command(label="Salir", command=salirAplicacion)

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

cuadro_id=Entry(mi_frame_01)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame_01)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="right")

cuadro_pass=Entry(mi_frame_01)
cuadro_pass.grid(row=2, column=1, padx=10, pady=10)
cuadro_pass.config(show="*")

cuadro_apellido=Entry(mi_frame_01)
cuadro_apellido.grid(row=3, column=1, padx=10, pady=10)

cuadro_direccion=Entry(mi_frame_01)
cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

texto_comentario=Text(mi_frame_01, width=16, height=5)
texto_comentario.grid(row=5, column=1, padx=10, pady=10)

scroll_vert=Scrollbar(mi_frame_01, command=texto_comentario.yview)
scroll_vert.grid(row=5, column=2, sticky="nsew")

texto_comentario.config(yscrollcommand=scroll_vert.set)





#-------------------- Label --------------------#
id_label=Label(mi_frame_01, text="ID:")
id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

nombre_label=Label(mi_frame_01, text="Nombre:")
nombre_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

pass_label=Label(mi_frame_01, text="Password:")
pass_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

apellido_label=Label(mi_frame_01, text="Apellido:")
apellido_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

direccion_label=Label(mi_frame_01, text="Direccion:")
direccion_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

comentarios_label=Label(mi_frame_01, text="Comentarios:")
comentarios_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")





#--------------------Botones--------------------#
mi_frame_02=Frame(root)
mi_frame_02.pack()

boton_crear= Button(mi_frame_02, text="Create")
boton_crear.grid(row=0, column=0, padx=10, pady=10, sticky="e")

boton_leer= Button(mi_frame_02, text="Read")
boton_leer.grid(row=0, column=1, padx=10, pady=10, sticky="e")

boton_actualizar= Button(mi_frame_02, text="Update")
boton_actualizar.grid(row=0, column=2, padx=10, pady=10, sticky="e")

boton_borrar= Button(mi_frame_02, text="Delete")
boton_borrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")




root.mainloop()
##########################################################################################################################