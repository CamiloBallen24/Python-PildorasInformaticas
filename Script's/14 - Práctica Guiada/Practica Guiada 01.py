#Practica guiada


##########################################################################################################################
from tkinter import *
from tkinter import messagebox
import sqlite3
##########################################################################################################################






##########################################################################################################################
#Funciones
#--------------------------------------------------#
def conexionBBDD():
	mi_conexion=sqlite3.connect("Usuarios")

	mi_cursor=mi_conexion.cursor()

	try:
		mi_cursor.execute('''
			CREATE TABLE DATOS_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(10),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD Creada con éxito")

	except:
		messagebox.showwarning("BBDD", "¡Atencion!, la BBDD ya existe")



#--------------------------------------------------#
def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

	if valor == "yes":
		root.destroy()



#--------------------------------------------------#
def limpiarCampos():
	mi_ID.set("")
	mi_nombre.set("")
	mi_apellido.set("")
	mi_direccion.set("")
	mi_pass.set("")
	texto_comentario.delete(1.0, END)



#--------------------------------------------------#
def crear():
	mi_conexion= sqlite3.connect("Usuarios")

	mi_cursor= mi_conexion.cursor()

	datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get(), texto_comentario.get("1.0", END)

	mi_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", datos)

	"""
	mi_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + mi_nombre.get() + 
		"','" + mi_pass.get() +  
		"','" + mi_apellido.get() + 
		"','" + mi_direccion.get() + 
		"','" + texto_comentario.get("1.0", END)+ "')")
	"""

	mi_conexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con exito")



#--------------------------------------------------#
def leer():
	mi_conexion= sqlite3.connect("Usuarios")

	mi_cursor= mi_conexion.cursor()

	mi_cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID =" + mi_ID.get())

	datos_usuarios = mi_cursor.fetchall()

	for usuario in datos_usuarios:
		mi_ID.set(usuario[0])
		mi_nombre.set(usuario[1])
		mi_pass.set(usuario[2])
		mi_apellido.set(usuario[3])
		mi_direccion.set(usuario[4])
		texto_comentario.insert(1.0, usuario[5])

	mi_conexion.commit()



#--------------------------------------------------#
def actualizar():
	mi_conexion= sqlite3.connect("Usuarios")

	mi_cursor= mi_conexion.cursor()
	
	datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get(), texto_comentario.get("1.0", END)

	mi_cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = ?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=" +mi_ID.get()+ " ", datos)

	"""
	mi_cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = '" + mi_nombre.get() + 
		"', PASSWORD = '" + mi_pass.get() +
		"', APELLIDO = '" + mi_apellido.get() +
		"', DIRECCION = '" + mi_direccion.get() +
		"', COMENTARIOS = '" + texto_comentario.get("1.0", END) + 
		"' WHERE ID =" + mi_ID.get() + "")
	"""
	mi_conexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con exito")


#--------------------------------------------------#
def eliminar():
	mi_conexion= sqlite3.connect("Usuarios")

	mi_cursor= mi_conexion.cursor()

	mi_cursor.execute("DELETE FROM DATOS_USUARIOS  WHERE ID =" + mi_ID.get() + "")

	mi_conexion.commit()

	messagebox.showinfo("BBDD", "Registro eliminado con exito")



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
borrar_menu.add_command(label="Borrar Campos", command=limpiarCampos)


crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=eliminar)

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

mi_ID=StringVar()
mi_nombre=StringVar()
mi_apellido=StringVar()
mi_pass=StringVar()
mi_direccion=StringVar()


cuadro_id=Entry(mi_frame_01, textvariable=mi_ID)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame_01, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="red", justify="right")

cuadro_pass=Entry(mi_frame_01, textvariable=mi_pass)
cuadro_pass.grid(row=2, column=1, padx=10, pady=10)
cuadro_pass.config(show="*")

cuadro_apellido=Entry(mi_frame_01, textvariable=mi_apellido)
cuadro_apellido.grid(row=3, column=1, padx=10, pady=10)

cuadro_direccion=Entry(mi_frame_01, textvariable=mi_direccion)
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

boton_crear= Button(mi_frame_02, text="Create", command=crear)
boton_crear.grid(row=0, column=0, padx=10, pady=10, sticky="e")

boton_leer= Button(mi_frame_02, text="Read", command=leer)
boton_leer.grid(row=0, column=1, padx=10, pady=10, sticky="e")

boton_actualizar= Button(mi_frame_02, text="Update", command=actualizar)
boton_actualizar.grid(row=0, column=2, padx=10, pady=10, sticky="e")

boton_borrar= Button(mi_frame_02, text="Delete", command=eliminar)
boton_borrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")




root.mainloop()
##########################################################################################################################