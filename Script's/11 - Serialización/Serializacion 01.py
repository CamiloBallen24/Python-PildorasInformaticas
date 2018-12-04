#TEMA: SERIALIZACION

#La serializacion consiste en guardar estructuras en un archivo binario
#y luego poder recuperarlos
############################################################################
import pickle
############################################################################


############################################################################
#Lista que queremnos guardar
listaNombres=["Camilo", "Andres", "Angie", "Pedro"]

#Fichero donde lo guardaremos
ficheroBinario=open("lista_nombres", "wb")

#Volcado (Guardado informacion)
pickle.dump(listaNombres, ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)
############################################################################

############################################################################
#Recuperamos la lista volcada anteriormente

ficheroBinario=open("lista_nombres", "rb")

#Cargamos o recuperamos la informacio 
listaNombres02=pickle.load(ficheroBinario)

print(listaNombres02)

############################################################################



