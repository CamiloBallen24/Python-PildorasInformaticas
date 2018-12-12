#TEMA: Rangos

######################################################################
import re
######################################################################


######################################################################
#Ejemplo #1
print("Ejemplo #1")

lista_nombres =['Ana', 'Pedro', 'Maria', 'Rosa', 'Sandra', 'Celia']

# O-T, es quivalente a O P Q R S T

for elemento in lista_nombres:
	if re.findall('^[O-T]', elemento):
		print(elemento)

print("\n\n\n")
######################################################################

######################################################################
#Ejemplo #2
print("Ejemplo #2")


lista_nombres =['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'Ma5', 'MaB', 'MaC']

#Me imprimira Ma1, Ma2, Ma3
for elemento in lista_nombres:
	if re.findall('Ma[0-3]', elemento):
		print(elemento)

print("\n")		



# ^0-3, todo menos el rango de 0 a 3, negacion
#Me imprimira Ma4, Ma4, MaA, MaB, MaC
for elemento in lista_nombres:
	if re.findall('Ma[^0-3]', elemento):
		print(elemento)

print("\n")	



#Dos Rango de 0 a 3 y de A a B -> 123AB
#Imprimira Ma1, Ma2, Ma3, MaA, MaB
for elemento in lista_nombres:
	if re.findall('Ma[0-3A-B]', elemento):
		print(elemento)


######################################################################