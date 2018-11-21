#TEMA: ELSE y ELIF
#ELSE -> y si no es verdad hara...


###########################################################################
#Uso de else y elif simple
print("Ejemplo #1")

print("Verificacion de Acceso:")
edadUsuario=int(input("Ingrese su edad: "))

if edadUsuario<18:
	print("No puedes pasar")
elif edadUsuario>110:
	print("Edad Incorrecta")
else:
	print("Puedes pasar")

print()
print("Vericacion Finalizada")	
print()
print()
print()

###########################################################################
#Uso de varios elif 
print("Ejemplo #2")

print("Verificacion de Nota:")
notaUsuario=int(input("Ingrese su nota: "))

if notaUsuario<5:
	print("Insuficiente")

elif notaUsuario<6:
	print("Suficiente")

elif notaUsuario<7:
	print("Bien")	

elif notaUsuario<9:
	print("Notable")

else:
	print("Sobresaliente")

print()
print("Vericacion Finalizada")	
print()
print()
print()