''' Amplía el ejercicio anterior para que modifique todas las apariciones del
 primer carácter por ‘$’. Por ejemplo, la palabra “cocotero” quedaría como 
 “$o$otero”.'''
 
 #Inicializacion
 
palabra_3 = input("Cual es la palabra? ")

#OPERACIONES

palabra_3 = palabra_3.replace(palabra_3[0],"$")

#SALIDAS
print("Cambiando las apariciones del 1º caracter por '$': {}"\
      .format(palabra_3))
