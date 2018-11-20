#TEMA:DICCIONARIOS
#Es una estructura con una asociacion clave:valor.
#A cada valor que se almacena se le asigna una clave unicos
#El orden da lo mismo
#Almacena todo tipo de valor


###########################################################################
#Diccionario Basico
print("Ejemplo #1")
miDiccionario ={"Espana":"Madrid", "Alemania":"Berlin", "Francia":"Paris"}
print(miDiccionario)
print()
print()
print()


###########################################################################
#Acceder a los elemnto
print("Ejemplo #2")
print(miDiccionario["Francia"])
print(miDiccionario["Espana"])
print()
print()
print()


###########################################################################
#Agregar elemento
print("Ejemplo #3")
miDiccionario["Italia"]="Roma"
miDiccionario["Reino Unido"] = "Londres"
print(miDiccionario)
print()
print()

###########################################################################
#Modificar elemento
print("Ejemplo #4")
miDiccionario["Portugal"] = "Lima" #Agrega
print(miDiccionario)
miDiccionario["Portugal"] = "Lisboa" #Modifica
print(miDiccionario)
print()
print()
print()

###########################################################################
#Eliminar elementos
print("Ejemplo #5")
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)
print()
print()
print()

###########################################################################
#Diccionario con varios elementos
print("Ejemplo #6")
miDiccionario = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario)
print()
print()
print()

###########################################################################
#Las claves en una tupla
print("Ejemplo #7")
miTupla = ["Espana", "Francia", "Reino Unido"]
miDiccionario={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres"}
print(miDiccionario)
print()
print()
print()

###########################################################################
#Diccionadio que almacena tuplas
print("Ejemplo #8")
miDiccionario = {23:"Jordan", "Nombre":"Mikel", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario)
print(miDiccionario["Anillos"])
print()
print()
print()

###########################################################################
#Diccionario en un diccionario
print("Ejemplo #9")
miDiccionario = {23:"Jordan", "Nombre":"Mikel", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario)
print(miDiccionario["Anillos"])
print()
print()
print()

###########################################################################
#Regresas las claves
print("Ejemplo #9")
print(miDiccionario.keys())
print()
print()
print()

###########################################################################
#Regresa los valores
print("Ejemplo #10")
print(miDiccionario.values())
print()
print()
print()