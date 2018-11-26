#TEMA: HERENCIA

#La herencia nos permite heredar(dotar) de las caracteristicas
#y metodos de una clase padre a una clase hijo. Permite ahorrar
#codigo

################################################################
#Clase Padre
class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha=True
		
	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca)
		print("Modelo: ", self.modelo)
		print("En Marcha: ", self.enMarcha)
		print("Acelerando: ", self.acelera)
		print("Frenando: ", self.frena)

################################################################


################################################################
#Clase Hijo
class Moto(Vehiculos): #Moto herada de vehiculo
	pass
################################################################


################################################################
print("Ejemplo #1")
miMoto= Moto("Honda", "CBR")
miMoto.estado()
print()
print()
print()
################################################################