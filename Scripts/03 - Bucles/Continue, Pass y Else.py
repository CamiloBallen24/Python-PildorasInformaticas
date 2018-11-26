#TEMA: Continue, Pass y Else

#######################################################
#Continue -Termina una iteracion, es decir se salta lo que queda de una  iteracion
print("Ejemplo #1")

for letra in "Python":
	if letra=='h':
		continue 
	print("Viendo la letra: " + letra)

print()
print()
print()

#######################################################
#Ejemplo de continue - No cuenta los espacios en blanco
print("Ejemplo #3")

nombre="Pildoras Informaticas"
contador = 0

for i in nombre:
	if i == ' ':
		continue
	contador+=1		

print(contador)
print()
print()
print()


#######################################################
#Break - Else
#El else se ejecuta cuando, el ciclo se ha terminado de  
#recorre por completo, si termina antes por un break, no lo
#ejecutara
print("Ejemplo #4")
print()

email= input("Introduce tu email, por favor: ")
print()

for i in email:
	if i=="@":
		arroba=True
		break
else:
	arroba=False

print("Valor de arroba: ", arroba)
print()
print()
print()


#######################################################
#Pass - Retorna un None, que nos ayuda a varias cosas, 
#la mas comun es definir partes de codigo 
#(if, funciones, bucles, clases) vacios sin generar errores

print("Ejemplo #5")
while True: #Ciclo infinito
	pass
print()
print()
print()