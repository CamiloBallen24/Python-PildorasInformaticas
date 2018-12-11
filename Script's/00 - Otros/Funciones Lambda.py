#TEMA: Funciones Lambda

#Son funciones anonimas que se usan para resumir. 

################################################################
def areaTriangulo(base, altura):
	return (base*altura)/2

################################################################


################################################################
#Ejemplo 1
#Usando la funcion definida
triangulo_01=areaTriangulo(7,5)
print(triangulo_01)
print()

#Usando las funciones lambdas
area_triangulo = lambda base, altura: (base*altura)/2

triangulo_02 = area_triangulo(7,5)
triangulo_03 = area_triangulo(9,6)

print(triangulo_02)
print(triangulo_03)
print()
print()
print()
################################################################


################################################################
#Ejemplo 2
al_cubo = lambda numero:pow(numero, 3)
print(al_cubo(13))
print()
print()
print()
################################################################


###############################################################
#Ejemplo 3
destacar_valor=lambda comision:"$¡{}!".format(comision)

comision_ana = 15585

print(destacar_valor(comision_ana))
################################################################