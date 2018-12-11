#TEMA: Funcion Filter

#Paragidma de programacion funcional


######################################################################################################################################################
#Ejemplo #1
def numeroPar(num):
	if num % 2 == 0:
		return True
######################################################################################################################################################


######################################################################################################################################################
numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numeroPar, numeros)))

#Resumir aun mas
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))
print()
print()
print()
######################################################################################################################################################





######################################################################################################################################################
#Ejemplo #2
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):
		return "{} que trabajo como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
######################################################################################################################################################

######################################################################################################################################################
lista_empleados=[
	Empleado("Juan", "Director", 75000),
	Empleado("Ana", "Presidenta", 85000),
	Empleado("Antonio", "Administrativo", 25000),
	Empleado("Sara", "Secretaria", 15000),
	Empleado("Mario", "Botones", 7000)
]

salarios_altos=filter(lambda empleado: empleado.salario > 50000, lista_empleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)
###########################################################################