#TEMA: PUNTERO EN UN ARCHIVO

################################################################################
from io import open
################################################################################


################################################################################
archivoTexto = open("archivo.txt", "r")

#La instruccion seek(n), nos situa el cursor en la posicion n
archivoTexto.seek(14) 
print(archivoTexto.read())
print()

#read(n), nos permite leer el texto hasta la posicion n, y mueve el puntero
archivoTexto.seek(0) 
print(archivoTexto.read(14))
print()
print()
print()

archivoTexto.close()
################################################################################


################################################################################
#readline() -> Retorna una sola linea
################################################################################

################################################################################
#Abrir el archivo en lectura y escritura
archivoTexto = open("archivo.txt", "r+") 

listaTexto = archivoTexto.readlines()

listaTexto[1]="Esta linea a sido incluida desde el exterior\n"

archivoTexto.seek(0)

archivoTexto.writelines(listaTexto)

################################################################################