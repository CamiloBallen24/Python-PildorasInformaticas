#TEMA: FOR

#######################################################
#Recorrer una lista
print("Ejemplo #1")
for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
	print(i)
print()
print()
print()


#######################################################
#Recorrer un String
print("Ejemplo #2")
miEmail="Camilo@gmail.com"
for i in miEmail:
	print(i, end='-')
print()
print()
print()


#######################################################
#For usando Range
print("Ejemplo #3")
for i in range(5):
	print(f"valor de la variable {i}") #Manera de Concatenar f indica que {i} sera un valor que varia 
print()
print()
print()


#######################################################
#For de range con un intervalo
print("Ejemplo #4")
for i in range(5,50,3): #Inicia en 5 hasta el 49, avanzando de 3 en 3
		print(f"valor de la variable {i}") 
print()
print()
print()

