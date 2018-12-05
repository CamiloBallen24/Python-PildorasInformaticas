#TEMA: AGREGAR VARIOS REGISTROS

#################################################################
import sqlite3
#################################################################


#################################################################
#Creamos base de datos y conexion
#Si la base de datos existe solo debemos conectarnos
mi_conexion= sqlite3.connect("Primera_base")

#Creamos el cursor o puntero
mi_cursor = mi_conexion.cursor()

#Agregamos varios Datos

varios_productos = [ 
	("Camiseta", 10, "Deportes"), 
	("Jarrón", 90, "Ceramica"),
	("Camion", 20, "Jugueteria"), 
	("Carro", 15, "Jugueteria")
]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos)

#Confirmamos los cambios
mi_conexion.commit()


#Cerramos el cursor o puntero


#Cerramos la conexion
mi_conexion.close()
#################################################################