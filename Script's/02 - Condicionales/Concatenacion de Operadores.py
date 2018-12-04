#TEMAS: -Concatenacion de operadores de comparacion




#######################################################
#Condicional Simple
print("Ejemplo #1")
edad=7
if 0<edad<100: # 0<edad and edad<100
	print("Edad Correcta")
else:
	print("Edad Incorrecta")	
print()
print()
print()

#######################################################
#Comdicional 
print("Ejemplo #2")
salarioPresidente = int(input("Introduce salario Presidente: "))
print("Salario Presidente: ", salarioPresidente)
print()

salarioDirector = int(input("Introduce salario Director: "))
print("Salario Director: ", salarioDirector)
print()

salarioJefeArea = int(input("Introduce salario Jefe Area: "))
print("Salario Jefe Area: ", salarioJefeArea)
print()

salarioAdministrativo = int(input("Introduce salario Administrativo: "))
print("Salario Administrativo: ", salarioAdministrativo)
print()

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("Todo funciona correctamente")	
else:
	print("Algo falla en esta empresa")
print()
print()
print()
print()
print()