#TEMA: AGREGAR UN REGISTRO

#################################################################
import sqlite3
#################################################################


#################################################################
#Creamos base de datos y conexion
#Si la base de datos existe solo debemos conectarnos
mi_conexion= sqlite3.connect("Primera_base")

#Creamos el cursor o puntero
mi_cursor = mi_conexion.cursor()

#Agregamos datos
mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#Confirmamos los cambios
mi_conexion.commit()


#Cerramos el cursor o puntero


#Cerramos la conexion
mi_conexion.close()
#################################################################