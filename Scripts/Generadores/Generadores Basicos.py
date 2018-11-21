#TEMA:GENERADORES

######################################################################
#Funcion que me regresa un numero determinado de numeros pares

def generaParesFuncion(limite):
	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)
		num = num+1

	return miLista
######################################################################	



######################################################################	
print("Ejemplo #1")
print(generaParesFuncion(10)) 
print()
print()
print()
print()
######################################################################	


######################################################################
#Generador que hace lo mismo que el ejemplo anterior
def generaPares(limite):
	num=1
	
	while num<limite:
		yield num*2	
		num = num+1
######################################################################	


######################################################################	
print("Ejemplo #2")
miGenerador = generaPares(10) #Creo mi generdor
for i in miGenerador:
	print(i)
print() 
print()
print()
print()
print()
######################################################################	


######################################################################
#Otro Uso del generador
print("Ejemplo #3")
miGenerador02= generaPares(12)

print("Primera llamada")
print(next(miGenerador02))
print()

print("Segunda llamada")
print(next(miGenerador02))
print()

print("Tercera llamada")
print(next(miGenerador02))
print()


print()
print()
print()
print()
######################################################################