#TEMA: Match y Search

######################################################################
import re
######################################################################


######################################################################
#Ejemplo #1
print("Ejemplo #1")
nombre_01="Sandra Lopez"
nombre_02="Antonio Gomez"
nombre_03="Maria Lopez"
nombre_04="Jara Lopez"
nombre_05="Lara Lopez"

cadena_01 = '214234143'

#La funcion match simpre busca al inicio de una cadena

#No distinguir entre mayusculas y minusculas
if re.match("sandra", nombre_01, re.IGNORECASE):
	print("Hemos encontrado el nombre\n\n")
else:
	print("No lo hemos encontrado\n\n")	



#Comodin del punto (.), cualquiere caracter
if re.match(".ara", nombre_04):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")	

if re.match(".ara", nombre_05):
	print("Hemos encontrado el nombre\n\n")
else:
	print("No lo hemos encontrado\n\n")	


#Mirar si una cadena empiza por un numero o no
if re.match("\d", cadena_01):
	print("Hemos encontrado el numero\n\n\n")
else:
	print("No lo hemos encontrado\n\n\n")	

######################################################################


######################################################################
#Ejemplo #2
print("Ejemplo #2")

#Search busca en cualquier parte de la cadena
if re.search("Lopez", nombre_04):
	print("Hemos encontrado el apellido\n\n")
else:
	print("No lo hemos encontrado\n\n")	


#Buscando en cadenas super largas
codigo_01 = "dvjkdbcxlvbksfdjlvbjladfs710321947322e2 sld c"
codigo_02 = "jds,sbajcksdjckcby23487319451471djf8ewrewd	 dcjKCB"
codigo_03 =  "JCDKVJBCVBBLBJKXCBKJVLBXCBVBBLJKCXicdshci2183s"


if re.search("71", codigo_01):
	print("Hemos encontrado el numero")
else:
	print("No lo hemos encontrado")	


if re.search("71", codigo_02):
	print("Hemos encontrado el numero")
else:
	print("No lo hemos encontrado")	


if re.search("71", codigo_03):
	print("Hemos encontrado el numero\n\n")
else:
	print("No lo hemos encontrado\n\n")		


######################################################################