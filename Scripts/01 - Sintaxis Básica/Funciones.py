#TEMA:FUNCIONES

#Sintaxis
#def nombre_funion(Parametros):
	#Instrucciones de la Funcion
	#return ->Opcional

#Existen funciones predifinidas -> Vienen con el Lenguaje

############################################################
#Declaracion de la funcion
def mensaje():
	print("Estamos aprendiendo Python")
	print("Estamos aprendiendo Instrucciones Basicas")
	print("Poco a poco iremos aprendiendo")


#Llamada de la funcion
mensaje()
print()
mensaje()
print()
print()
print()

############################################################
#Funciones con Argumentos
def suma(num1, num2):
	print(num1+num2)

#Llamada de la funcion
suma(5,7)
suma(35,338)
suma(123,21321)
print()
print()
print()

############################################################
#Funciones con Retorno de Valor
def suma2(num1, num2):
	resultado = num1+num2
	return resultado

#Llamada de la funcion
print(suma2(5,7))
print(suma2(35,338))
print(suma2(123,21321))
print()
print()
print()