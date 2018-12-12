#TEMA: Expresiones Regulares

#Son secuencia de Caracteres que forman un patron de busqueda.

######################################################################
import re
######################################################################



######################################################################
cadena = "Vamos a aprender expresiones regulares"

#Buscar una subcadena en una cadena
#Si esta retorna un objeto, si no retorna none
print(re.search("aprender", cadena)) 
print()
print()
print()

#El metodo star nos dice donde comienza el texto encontrado
texto_encontrado = re.search("aprender", cadena)
print(texto_encontrado.start())
print()

#El metodo end nos dice donde texto el texto encontrado
print(texto_encontrado.end())
print()

#El metodo span nos devuelve en una tupla el inicio y el fin
print(texto_encontrado.span())
print()
print()
print()
######################################################################

######################################################################
#Cuantas veces esta una subcadena en una cadena
cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje sencillo"

texto_buscar="Python"

print(len(re.findall(texto_buscar, cadena)))
######################################################################