#TEMA: Identificador (ID) Autoincrementable

###############################################################
import sqlite3
###############################################################

###############################################################
mi_conexion = sqlite3.connect("Gestion_productos_02")

mi_cursor=mi_conexion.cursor()

#Creacion tabla
mi_cursor.execute('''
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

#Archivos a insertar
productos = [
	
	("Pelota", 20, "Jugueteria"),
	("Pantalon", 15, "Confección"),
	("Destornillador", 25, "Ferretería"),
	("Jarrón", 45, "Cerámica")
	
]

#Insercion
mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos)



mi_conexion.commit()

mi_conexion.close()
###############################################################