#TEMA: POLIMORFISMO

###########################################################################
class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")
###########################################################################

###########################################################################
class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")			
###########################################################################

###########################################################################
class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")
###########################################################################

###########################################################################
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

###########################################################################


###########################################################################
print("Ejemplo #1")

miVehiculo01=Moto()
desplazamientoVehiculo(miVehiculo01)				
print()

miVehiculo02=Coche()
desplazamientoVehiculo(miVehiculo02)
print()

miVehiculo03=Camion()
desplazamientoVehiculo(miVehiculo03)		
print()
###########################################################################