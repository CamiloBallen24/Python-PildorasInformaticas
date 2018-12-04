#TEMA: SERIALIZACION

#Serializacion de objetos
############################################################################
import pickle
############################################################################


############################################################################
class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True
	
	def estado(self):
		print("Marca:", self.marca)
		print("Modelo:", self.modelo)
		print("En marcha:", self.enMarcha)
		print("Acelerando:", self.acelera)
		print("Frenando:", self.frena)

############################################################################


############################################################################
#Serializaremos los siguientes objetos

coche01=Vehiculo("Mazda", "XSA")
coche02=Vehiculo("Mazda", "001")
coche03=Vehiculo("RENAULT", "X")

coches=[coche01, coche02, coche03]

fichero=open("los_coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

############################################################################


############################################################################
#Rescatando informacion

fichero = open("los_coches", "rb")

misCoches= pickle.load(fichero)

fichero.close()

for coche in misCoches:
	coche.estado()
	print()
	print()
	print()
############################################################################


