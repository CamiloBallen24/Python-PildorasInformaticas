#TEMA: TUPLAS
#Las tuplas son LISTAS INMUTABLES
#No permiten añadir, eliminar, mover elementos
#No permiten busquedas (En python3 si), solo verficar si un elemento esta contenido o no
#Permiten extraer partes
#Formatean cadenas

#Sintaxis
#nombreTupla=(elem1, elem2, elem3...)

###########################################################################
#Una tupla sencilla
print("Ejemplo #1")
miTupla=("Camilo", 24, 4, 2000) #Creamos una tupla
print(miTupla[2]) #Acceder a un elemento
print()
print()
print()

###########################################################################
#De tuplas a listas 
print("Ejemplo #2")
miLista = list(miTupla) #De lista a tupla
print(miLista) #Imprimimos la lista
print()
print()
print()


############################################################################
#De lista a tupla
print("Ejemplo #3")
miLista=[1,2,3,4,5,6,7,8,9] 
miTupla=tuple(miLista)
print(miTupla)
print()
print()
print()


###########################################################################
#Contenido o no
print("Ejemplo #4")
miTupla=(12, 3213, 213, True)
print(0 in miTupla)
print(12 in miTupla)
print()
print()
print()

###########################################################################
#Cuantas veces esta un elemento
print("Ejemplo #5")
miTupla = (1,2,3,3,3,3,4)
print(miTupla.count(3))
print()
print()
print()


###########################################################################
#Longitud de una tupla
print("Ejemplo #6")
miTupla=(12,123,3,213,21)
print(len(miTupla))
print()
print()
print()


###########################################################################
#Tuplas unitarias
print("Ejemplo #7")
miTupla=("Camilo",) #La coma es importante
print(len(miTupla))
print()
print()
print()



###########################################################################
#Tupla sin parentesis
print("Ejemplo #8")
miTupla = 12,3123,214,True, "Sofia" #Empaquetado de tupla
print(miTupla)
print()
print()
print()



###########################################################################
#Desenpaquetado de tuplas
print("Ejemplo #9")
miTupla = "Juan", 12, 12, 2000
nombre, dia, mes, ano = miTupla
print(nombre)
print(dia)
print(mes)
print(ano)
print()
print()
print()










