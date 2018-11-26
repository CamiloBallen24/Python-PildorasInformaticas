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
	hacerCaballito = ""
	def caballito(self):
		self.hacerCaballito = "Voy haciendo Caballito"


	def estado(self):
		print("Marca: ", self.marca)
		print("Modelo: ", self.modelo)
		print("En Marcha: ", self.enMarcha)
		print("Acelerando: ", self.acelera)
		print("Frenando: ", self.frena)
		print(self.hacerCaballito)
################################################################



################################################################
#Clase Hijo
class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado = cargar
		
		if(self.cargado):
			return "La Furgoneta esta caragda"

		else:
			return "La Furgoneta no esta cargada"
################################################################

################################################################
#Clase padre #2
class VehiculosElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia = 100
	
	def cargarEnergia(self):
		self.cargando = True		
################################################################

################################################################
#Herencia Multiple
#En caso de que las clases padres tengan metodos iguales, se
#le da preferencia al metodo de la clase que esta mas a la izquierda
class BicicletaElectrica(VehiculosElectricos): 
	pass

################################################################



################################################################
print("Ejemplo #1")
#Instancia de Moto
miMoto= Moto("Honda", "CBR")

#Llamamos un metodo propio
miMoto.caballito()

#Llamamos un metodo que heredo y posteriormente lo sobre escribio
miMoto.estado()

print()
print()
print()
################################################################

################################################################
print("Ejemplo #2")
#Instancia de Furgoneta
miFugoneta = Furgoneta("Renault", "Kangoo")

#Lllama metodos heredados
miFugoneta.arrancar()
miFugoneta.estado()

#Llama un metodo propio
print(miFugoneta.carga(True))


print()
print()
print()
################################################################

################################################################
print("Ejemplo #3")
miBici = BicicletaElectrica("Orbea", "HC1030")

miBici.estado()
print()
print()
print()
################################################################
