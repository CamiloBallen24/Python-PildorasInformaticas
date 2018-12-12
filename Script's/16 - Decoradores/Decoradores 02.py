#TEMA: Decoradores

#Funciones que a su vez añaden funcionalidades a otras funciones

######################################################################
def funcionDecoradora(funcionParametro):

	def funcionInterior(*args, **kwargs):
	
		#Aciones adicionales que decoran
		print("Vamos a realizar un calculo")

		#Funcion Original
		funcionParametro(*args, **kwargs)

		#Aciones adicionales que decoran
		print("Hemos Realizado el calculo\n\n")

	return funcionInterior		
######################################################################


######################################################################
@funcionDecoradora
def suma(num_01, num_02):
	print(num_01 + num_02)
######################################################################


######################################################################
@funcionDecoradora
def resta(num_01, num_02):
	print(num_01 - num_02)
######################################################################



######################################################################
@funcionDecoradora
def potencia(base, exponente):
	print(pow(base, exponente))

######################################################################

######################################################################
suma(432,432)
resta(23,4523)
potencia(base=5, exponente=3)
######################################################################