#TEMA: POO-CLASES
#      Clase Basica

#Un clase es la plantilla, de los objetos o intancias
########################################################################
#Definicion de una clase
class Coche():
	#Atributos o Propiedades
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	#Metodos
	def arrancar(self): #Self hace referencia a la instancia de la clase
		self.enMarcha=True
	
	def estado(self):
		if (self.enMarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"
########################################################################


########################################################################
#Instanciar la clase
print("Ejemplo #1")
miCoche=Coche()

#Accediendo a las Propiedades o Atributos
print("El largo del coche es", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, "ruedas")

#Lllamando los metodos
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())

print()
print()
print()
print()
print()
########################################################################