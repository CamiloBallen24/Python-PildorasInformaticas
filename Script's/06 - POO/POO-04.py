#TEMA: SUPER

############################################################
class Persona():
	def __init__(self, nombre, edad, lugarResidencia):
		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion(self):
		print("Nombre ", self.nombre)		
		print("Edad: ", self.edad)		
		print("Residencia: ", self.lugarResidencia)

############################################################


############################################################
class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, lugarEmpleado):
		#super() nos permite llamar al 
		#metodo __init__ de la clase padre
		super().__init__(nombreEmpleado, edadEmpleado, lugarEmpleado) 
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ", self.salario)
		print("Antiguedad: ", self.antiguedad)
############################################################		


############################################################
print("Ejemplo #1")

#Instancia de empleado
Antonio = Empleado(1500, 14, "Antonio", 55, "Colombia")
print()

#Llamamos un metodo heredado y sobreescrito
Antonio.descripcion()
print()

#Uso de isinstance
print(isinstance(Antonio, Persona))
print(isinstance(Antonio, Empleado))
############################################################


############################################################
#Principio de sustitucion -> "Es siempre un/a"

#Una subclase es siempre una superclase
#Ejemplo un empleado es siempre persona, pero una persona
#no siempre es empleado

#Python nos brinda is instance, nos permite determinar si 
#un objeto es una instancia de una clase o no
############################################################