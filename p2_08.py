'''3. Crea una lista vacía llamada “maleta”. 
a. Añade varios “ítems” secuencialmente (ej. gafas, calcetines…). 
b. Imprime el número de elementos de tu maleta y a continuación imprime la variable 
“maleta”, es decir, su contenido completo (como hiciste con los “animales”). 
c. Por último, imprime únicamente los dos primeros ítems, y a continuación los dos 
últimos. Pista: recuerda el famoso “slicing” con el uso de [X:Y]'''

#INICIALIZACION
maleta = []

#OPERACIONES

maleta.append(input("Adicione 1º item a la lista "))
maleta.append(input("Adicione 2º item a la lista "))
maleta.append(input("Adicione 3º item a la lista "))
maleta.append(input("Adicione 4º item a la lista "))

# SALIDAS
tamano = len(maleta)
print("\n\t item b")
print("la lista maleta tiene {} elementos".format(tamano))
print(maleta)

# OPERACIONES
dosPrimeros = maleta[:2]
dosUltimos = maleta[-1:-3:-1]

#SALIDAS
print("\n\t item c")
print("Los dos primeiros itens: {}".format(dosPrimeros))
print("Los dos ultimos itens: {}".format(dosUltimos))
