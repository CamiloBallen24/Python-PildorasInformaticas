#TEMA:WHILE

import math

#######################################################
#While Simple
print("Ejemplo #1")
i=1
while i<=10:
	print("Ejecucion " + str(i))
	i=i+1
print()
print()
print()
print()
print()

#######################################################
#While Realmente Indeterminado (Puede ser infinito)
print("Ejemplo #2")
print()
edad= int(input("Ingrese su edad: "))
print()

while edad<5 or edad>100:
	print("Has introducido unas edad Incorrecta. Vuelve a intertarlo")
	edad= int(input("Ingrese su edad: "))
	print()

print("Gracias por colaborar, puedes pasar.")
print("Edad: " + str(edad))

print()
print()
print()
print()
print()

#######################################################
#While indeterminado (Finito)
print("Ejemplo #3")
print()

print("Programa de Calculo de raiz cuadrada")
print()

numero = int(input("Introduce un numero por favor:"))
print()

intentos=0
while numero<0:
	print("No se puede hallar la raiz de un numero negativo.")

	if intentos==2:
		print("Has consumido demasiados intentos.")
		print("Fin del Programa")
		break
	
	if numero<0:
		intentos = intentos+1

	numero = int(input("Introduce un numero por favor:"))
	print()

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))


print()
print()
print()
print()
print()