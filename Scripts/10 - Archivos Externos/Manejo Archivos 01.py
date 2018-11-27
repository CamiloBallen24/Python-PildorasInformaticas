
#TEMA: MANEJO DE ARCHIVOS EXTERNOS

#Creacion -> Apertura -> Manipulacion -> Cierre
################################################################################
from io import open
################################################################################


################################################################################
#Podemos abrir archivo en tres modos con open()
#Lectura (r)-> Solo leer
#Escritura("w") -> Escribir sobre el archivo
#Append ("a")-> Escribir al final del archivo sin perder contenido
################################################################################

################################################################################
#Modo Escritura
#Abrrimos o creamos el archivo en modo escritura
#Creacion y apertura
#Si no existe el archivo open lo crea
archivoTexto = open("archivo.txt", "w") 

#Manipulacion
#Escribimos sobre el archivo
frase = "Estupendo dia para estudiar Python \nEl Martes"
archivoTexto.write(frase)

#Cerramos el flujo
archivoTexto.close()
################################################################################

################################################################################
#Modo Lectura
#Abrimos el archivo en modo lectura
archivoTexto = open("archivo.txt", "r")

#leemos todo el archivo
texto = archivoTexto.read()

#Cierre de flujo
archivoTexto.close()

print(texto)
print()
################################################################################

################################################################################
#Modo Lectura
archivoTexto = open("archivo.txt", "r")
#readlines() nos retorna una lista donde cada elemento es una linea del archivo
lineasTexto= archivoTexto.readlines()

#Cierre de flujo
archivoTexto.close()

print(lineasTexto)
print()
################################################################################

################################################################################
#Modo Append
archivoTexto = open("archivo.txt", "a")

archivoTexto.write("\nAunque siempre es un buen dia para estudiar Python")

archivoTexto.close()
################################################################################

