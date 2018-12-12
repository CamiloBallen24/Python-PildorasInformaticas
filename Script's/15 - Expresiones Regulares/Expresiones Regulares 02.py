#TEMA: Metacaracteres

#Anclas y clases de caracteres

####################################################################################
import re
####################################################################################


####################################################################################
#Usando Anclas
lista_nombres = ['Ana Gomez', 
				 'Maria Martin', 
				 'Sandra Lopez', 
				 'Santiago Martin', 
				 'Sandra Ferndadez']

# ^texto, decimos que nos busque una subcadena, pero que adicionalmente esta este en el inicio
# texto$, decimos que nos busque una subcadena, pero que adicionalmente esta este en el final
for elemento in lista_nombres:
	if re.findall('^Sandra', elemento):
		print(elemento)

	if re.findall('Martin$', elemento):
		print(elemento)	
print("\n\n")


# [caractes], decimos que si en una cadena se encuentran las caracteres 
#entre corchetes sin importar el orden. 
print(re.findall("[ñE]", "Español"))
print(re.findall("niñ[oa]s", "niños y niñas"))
print(re.findall("cami[oó]n", "camion y camión"))
####################################################################################