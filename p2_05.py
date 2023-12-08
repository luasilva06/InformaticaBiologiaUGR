'''5. Elimina el carácter “n-ésimo” de un string no vacío. Por ejemplo, si se
decide eliminar el carácter 4 de la palabra “Python” quedaría como “Pyton”.
¡Cuidado! No es directo “eliminar” datos para las cadenas de texto, 
hay que usar un pequeño truco.'''

#INICIALIZACION
cadena = input("Cual es la palabra? ")
carac = int(input("Cual es la posicion del caracter que quieres eliminar? "))

#OPERACIONES
nuevaCadena = cadena[:carac] + cadena[carac+1:]

#SALIDAS

print("Tu eliminó el caracter '{}' de la cadena '{}', entonces ahora es: {}"\
      .format(cadena[carac],cadena,nuevaCadena))
