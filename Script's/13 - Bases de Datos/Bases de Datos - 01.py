#TEMA: Bases de Datos

#################################################################
import sqlite3
#################################################################


#################################################################
#Creamos base de datos y conexion
#Si la base de datos existe solo debemos conectarnos
mi_conexion= sqlite3.connect("Primera_base")

#Creamos el cursor o puntero
mi_cursor = mi_conexion.cursor()

#Creamos una tabla
#mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Agregamos datos
#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#Agregamos varios Datos
'''
varios_productos = [ 
	("Camiseta", 10, "Deportes"), 
	("Jarrón", 90, "Ceramica"),
	("Camion", 20, "Jugueteria"), 
	("Carro", 15, "Jugueteria")
]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos)
'''

#Recibiendo datos
mi_cursor.execute("SELECT * FROM PRODUCTOS")


varios_productos=mi_cursor.fetchall() # -> Me regresa una lista con los productos

for producto in varios_productos:
	print("Nombre: ", producto[0], " \nPrecio: ", producto[1], " \nSeccion: ", producto[2], "\n\n")


#Confirmamos los cambios
mi_conexion.commit()



#Cerramos el cursor o puntero


#Cerramos la conexion
mi_conexion.close()
#################################################################