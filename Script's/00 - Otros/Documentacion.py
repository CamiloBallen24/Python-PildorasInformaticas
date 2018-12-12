class Areas:
	"""Esta clase calcula el area de diferentes figuras geometricas"""
	def areaCuadrado(lado):
		""" Aqui debe ir la explicacion de la funcion.

			Calcula el area de un cuadrado elevando al 
			cuadrado el parametro lado.
		"""
		return "El área del cuadrado es: " +  str(lado*lado)

	def areaTriangulo(base, altura):
		"""Calcula el area de un triangulo utilizando los parametro base y altura"""

		return "El área del triangulo es: " + str((base*altura)/2)


print(Areas.areaCuadrado(12))	
print("\n\n\n")

print(Areas.areaCuadrado.__doc__)
print("\n\n\n")

help(Areas.areaCuadrado)
print("\n\n\n")

help(Areas.areaTriangulo)
print("\n\n\n")

help(Areas)
print("\n\n\n")