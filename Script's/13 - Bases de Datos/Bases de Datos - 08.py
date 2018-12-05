#TEMA: CRUD

#Create Read Update Delete
##############################################################################################################################
import sqlite3
##############################################################################################################################



##############################################################################################################################
mi_conexion = sqlite3.connect("Gestion_productos_04")

mi_cursor=mi_conexion.cursor()

#------------------------Creacion tabla------------------------#

#mi_cursor.execute('''
#	CREATE TABLE PRODUCTOS(
#	ID INTEGER PRIMARY KEY AUTOINCREMENT,
#	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#	PRECIO INTEGER,
#	SECCION VARCHAR(20))
#''')



#------------------------Archivos a insertar------------------------#
#productos = [
#	
#	("Pelota", 20, "Jugueteria"),
#	("Pantalon", 15, "Confección"),
#	("Destornillador", 25, "Ferretería"),
#	("Jarrón", 45, "Cerámica")
#	
#]

#------------------------Insercion------------------------#
#mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos)




#------------------------SELECCION - READ------------------------#
mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION= 'Confección'")

productos = mi_cursor.fetchall()

print(productos)


#------------------------Update  o modificacion------------------------#
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO='35' WHERE NOMBRE_ARTICULO='Pelota'")



#------------------------DELETE------------------------#
mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=3")


#------------------------CONFIRMAR CAMBIOS ------------------------#
mi_conexion.commit()

#------------------------CERRAR CONEXION------------------------#
mi_conexion.close()
##############################################################################################################################