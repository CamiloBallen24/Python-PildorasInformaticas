#TEMA: CONSULTAR DATOS

#################################################################
import sqlite3
#################################################################


#################################################################
#Creamos base de datos y conexion
#Si la base de datos existe solo debemos conectarnos
mi_conexion= sqlite3.connect("Primera_base")

#Creamos el cursor o puntero
mi_cursor = mi_conexion.cursor()


#Recibiendo datos
mi_cursor.execute("SELECT * FROM PRODUCTOS")

#Me regresa una lista con los productos
varios_productos=mi_cursor.fetchall() 

#Mostrar Datos
for producto in varios_productos:
	print("Nombre: ", producto[0], " \nPrecio: ", producto[1], " \nSeccion: ", producto[2], "\n\n")


#Cerramos el cursor o puntero


#Cerramos la conexion
mi_conexion.close()
#################################################################