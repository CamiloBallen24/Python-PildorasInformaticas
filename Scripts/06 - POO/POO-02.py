#Tema: -Estado Inicial (Constructor)
#      -Encasuplacion (Atributos y Metodos)

#El estado inicial o contructor, nos permite determinar como
#sera el estado de al instancia, en el punto en el que se crea.

#La encapsulacion, nos permite ocultar al exterior (fuera de la clase)
#algunos atributos y metodos, los cuales por su funcionamiento no deben 
#ser llamados o accesidos desde afuera


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
			chequeo = self.__chequeoInterno()
	
		if (self.__enMarcha and chequeo):
			return "El coche esta en marcha"

		elif(self.__enMarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar"

		else:
			return "El coche esta parado"
	
	def estado(self):
		print("El coche tiene", self.__ruedas, "ruedas")
		print("Un ancho de", self.__anchoChasis)
		print("Un largo de", self.__largoChasis)
	

	#Metodo Ecapsulado
	#__nombreMetodo, solo se puede acceder dentro de la clase
	def __chequeoInterno(self):
		print("Realizando Chequeo Interno")

		self.gasolina = "ok"
		self.aceite= "ok"
		self.puertas = "cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False

########################################################## 


########################################################## 
print("Ejemplo #1")
print()

print("Coche 1")
miCoche01 = Coche()
miCoche01.estado()
print(miCoche01.arrancar(True))
print()
print()


print("Coche 2")
miCoche02 = Coche()
miCoche02.estado()
print(miCoche02.arrancar(False))

print()
print()
print()
########################################################## 

########################################################## 
# miVarible, es difente a __miVariable
########################################################## 