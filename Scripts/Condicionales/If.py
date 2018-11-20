#TEMA:IF

###########################################################################

def evalucion(nota):
	valoracion = "Aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion


###########################################################################	
#Llamada de la funcion
print("Ejemplo #1")
print(4)
print()
print()
print()

###########################################################################
#Tomar valor del teclado
print("Ejemplo #2")
notaAlumno= input("Introduce la nota del alumno: ") #Coge el valor por consola
notaAlumno = int(notaAlumno) #Convierte el valor a entero
print(evalucion(notaAlumno))
print()
print()
print()

##########################################
##Importantes el Ambito de las Variables##
##########################################


