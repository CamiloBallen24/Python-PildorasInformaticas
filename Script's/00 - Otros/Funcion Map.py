#TEMA: Funcion Map

#Map aplica a cada elemento de una lista una misma funcion
######################################################################################################################################################
#Ejemplo #1
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__(self):
		return "{} que trabajo como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
######################################################################################################################################################



######################################################################################################################################################
def calculoComision(empleado):
	empleado.salario = empleado.salario*1.03
	return empleado
######################################################################################################################################################



######################################################################################################################################################
lista_empleados_01=[
	Empleado("Juan", "Director", 7500),
	Empleado("Ana", "Presidenta", 8000),
	Empleado("Antonio", "Administrativo", 2500),
	Empleado("Sara", "Secretaria", 1500),
	Empleado("Mario", "Botones", 1000)
]


lista_empleados_02= map (calculoComision, lista_empleados_01)

for empleado in lista_empleados_02:
	print(empleado)
###########################################################################


