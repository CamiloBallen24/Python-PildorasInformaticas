#TEMA: GUARDADO PERMANENTE


#######################################################################
import pickle
#######################################################################


#######################################################################

class Persona():
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona con el nombre:", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)	

#######################################################################


#######################################################################

class ListaPersonas():
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)		

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		
		except:			
			print("El fichero esta vacio")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)		
#######################################################################

#######################################################################
miLista=ListaPersonas()

persona01 = Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona01)

persona02 = Persona("Valentina", "Femenino", 21)
miLista.agregarPersonas(persona02)

persona03 = Persona("Juan", "Masculino", 19)
miLista.agregarPersonas(persona03)

print()
miLista.mostrarPersonas()
#######################################################################