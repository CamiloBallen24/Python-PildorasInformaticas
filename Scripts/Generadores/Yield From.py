#TEMA: YIELD FROM
#Simplifica el codigo cuando se trabaja con bloques anidados

#Permite acceder a los subelementos, en caso de que los elementos
#Sean elementos iterables

######################################################################
def devuelve_cuidades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento
######################################################################

######################################################################
#Sin el Uso de Yield From
print("Ejemplo #1")

#Creo mi generador
ciudades_Devueltas= devuelve_cuidades("Madrid", "Barcelona", "Bilbao", "Valencia")

#Devuelve los caracteres de las ciudades
print(next(ciudades_Devueltas)) 
print(next(ciudades_Devueltas)) 
print(next(ciudades_Devueltas)) 
print(next(ciudades_Devueltas)) 
print(next(ciudades_Devueltas)) 
print(next(ciudades_Devueltas)) 

print()
print()
print()
print()
######################################################################



######################################################################
def devuelve_cuidades02(*ciudades):
	for elemento in ciudades:
		yield from elemento
######################################################################

######################################################################
#Con el Uso de Yield From
print("Ejemplo #2")

#Creo mi generador
ciudades_Devueltas02= devuelve_cuidades02("Madrid", "Barcelona", "Bilbao", "Valencia")

#Devuelve los caracteres de las ciudades
print(next(ciudades_Devueltas02)) 
print(next(ciudades_Devueltas02)) 
print(next(ciudades_Devueltas02)) 
print(next(ciudades_Devueltas02)) 
print(next(ciudades_Devueltas02)) 
print(next(ciudades_Devueltas02)) 

print()
print()
print()
print()
######################################################################