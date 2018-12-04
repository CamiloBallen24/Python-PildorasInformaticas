#Equivalentes a los Arrays -> En realidad son la EDA lista
#Permite almacenar varios valores
#Disintos tipos de variables
#Son dinamicas

#Sintaxis
#nombreLista = [elem1, elem2, elem3...]

#########################################################
print("Ejemplo #1")
miLista =["Camilo", "Tatiana", "Juan", "Marcos"]
print(miLista) #Imprime la lista
print()
print()
print()

#Acceder a un elemento
print("Ejemplo #2")
print(miLista[2]) 
print()
print()
print()

#Si el indicie es negativo comienza a contar desde el final
print("Ejemplo #3")
print(miLista[-3]) 
print()
print()
print()

#Acceder a una sublista
print("Ejemplo #4")
print(miLista[0:3]) 
print(miLista[:3]) #Abreviacion
print()
print()
print()

#Acceder a una sublista
print("Ejemplo #5")
print(miLista[1:3]) #Desde el indice 1 hasta el indice 2
print()
print() 
print() 

#Acceder a una sublista
print("Ejemplo #6")
print(miLista[2:]) #Desde el indice 2 hasta el final
print()
print()
print()

#Agregar Elemento
print("Ejemplo #7")
miLista.append("Andres") #Agrega el elemento al final
print(miLista)
print()
print()
print()


#Agregar Elemento en cualquie posicion
print("Ejemplo #8")
miLista.insert(2,"Sandra") #Agrega el elemento en la poscion dada
print(miLista)
print()
print()
print()

#Agregar Varios Elementos (Concatenar listas)
print("Ejemplo #9")
miLista.extend(["Ana", "Sofia"])
print(miLista)
print()
print()
print()


#Retornar el indice de una elemento
#Si hay dos elementos devuelve el primero que se encuentra
print("Ejemplo #10")
print(miLista.index("Ana"))
print()
print()
print()

#Un elemento se encuentra o no
print("Ejemplo #11")
print("Pepe" in miLista)
print()
print()
print()

#Eliminar Elemento
print("Ejemplo #12")
print(miLista)
miLista.remove("Ana")
print(miLista)
print()
print()
print()

#Eliminar el ultimo elemento de una lista
print("Ejemplo #13")
print(miLista)
miLista.pop()
print(miLista)
print()
print()
print()

#Sumar listas (Concatenar)
print("Ejemplo #14")
miLista = ["Maria", 5, True, 68.9]
miLista2 = ["Sandra", "Lucia"]
miLista3 = miLista+miLista2
print(miLista3)
print()
print()
print()

#Multiplicar listas
print("Ejemplo #15")
miLista = ["Maria", 5, True]*3
print(miLista)
print()
print()
print()