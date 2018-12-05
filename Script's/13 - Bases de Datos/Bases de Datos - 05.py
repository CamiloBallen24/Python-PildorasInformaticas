#TEMA: Identificador (ID)

###############################################################
import sqlite3
###############################################################

###############################################################
mi_conexion = sqlite3.connect("Gestion_productos")

mi_cursor=mi_conexion.cursor()

#Creacion tabla
mi_cursor.execute('''
	CREATE TABLE PRODUCTOS(
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

#Archivos a insertar
productos = [
	
	("AR01", "Pelota", 20, "Jugueteria"),
	("AR02", "Pantalon", 15, "Confección"),
	("AR03", "Destornillador", 25, "Ferretería"),
	("AR04", "Jarrón", 45, "Cerámica")
	
]

#Insercion
mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?, ?)", productos)



mi_conexion.commit()

mi_conexion.close()
###############################################################