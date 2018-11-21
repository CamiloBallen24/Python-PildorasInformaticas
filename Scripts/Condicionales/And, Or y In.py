#TEMA: AND, OR y IN

#######################################################
#Condicional (AND y OR)
print("Ejemplo #1")
print("Programa de Becas año 2099")
distanciaEscuela=int(input("Introduce la distancia a la escuela: "))
print(distanciaEscuela)
print()

numeroHermanos= int(input("Introduce el numero de hermanos en el centro: "))
print(numeroHermanos)
print()

salarioFamiliar = int(input("Introduce salario anual bruto: "))
print(salarioFamiliar)
print()

if (distanciaEscuela>40 and numeroHermanos>2) or salarioFamiliar<=20000:
	print("Tienes Derecho a Beca")
else:
	print("No tienes Derecho a Beca")	

print()
print()
print()
print()
print()


#######################################################
#Condiconal 2 (Uso de In)
print("Ejemplo #2")
print("Asignaturas Optativas año 2301")
print()

print("Informatica Grafica - Pruebas de Software - Usabilidad y Accsiblidad")
print()

opcion= input("Ingresa tu asignatura seleccionada: ")
print()

asignatura = opcion.lower()
if asignatura in {"informatica grafica", "pruebas de software",  "usabilidad y accesiblidad"}:
	print("Asignatura Elegida: " + opcion)
else:
	print("La asignatura escogida no esta contenida")

print()
print()
print()
print()
print()