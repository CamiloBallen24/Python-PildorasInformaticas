#TEMA - FINALLY y Otros
#El bloque que esta en finally se ejecutara, ya sea que ocurre un excepcion o no
#El Try nunca puede ir solo, debe ir acompañado de un Finally o de uno o varios except
##############################################################################
#Capturar varias excepciones de manera individual
def divide():
	try:
		op1=(float(input("Introduce el primer numero: ")))
		op2=(float(input("Introduce el segundo numero: ")))
	
		print("La division es: " + str(op1/op2))

	except ValueError:
		print("El valor introducido es erroneo")
	
	except ZeroDivisionError:
		print("No se puede dividir entre cero")		
	
	finally:		
		print("Calculo Finalizado")	
##############################################################################


##############################################################################
#Capturar todas las excepciones de las misma manera
def divide02():
	try:
		op1=(float(input("Introduce el primer numero: ")))
		op2=(float(input("Introduce el segundo numero: ")))
	
		print("La division es: " + str(op1/op2))

	except:
		print("Ah ocurrido un error")		
	
	finally:		
		print("Calculo Finalizado")	
	
##############################################################################


##############################################################################
#divide()
divide02()
##############################################################################