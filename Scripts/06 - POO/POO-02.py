#Tema: -Estado Inicial (Constructor)
#      -Encasuplacion


##########################################################
class Coche():
	#Nuestro Constructor
	def __init__(self):
		#__nombreVariable -> Nos permite encapsular el atributo 
		#Solo se puede acceder desde dentro de la clase
		self.__largoChasis=250 
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	def arrancar(self, arrancamos): 
		self.__enMarcha=arrancamos
	
		if (self.__enMarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"
	
	def estado(self):
		print("El coche tiene", self.__ruedas, "ruedas")
		print("Un ancho de", self.__anchoChasis)
		print("Un largo de", self.__largoChasis)
	
########################################################## 


########################################################## 
print("Ejemplo #1")

print()
print("Coche 1")
miCoche01 = Coche()
print(miCoche01.arrancar(True))
miCoche01.estado()

print()
print("Coche 2")
miCoche02 = Coche()
print(miCoche02.arrancar(False))
miCoche02.estado()

print()
print()
print()
print()
print()
########################################################## 

########################################################## 
# miVarible, es difente a __miVariable
########################################################## 