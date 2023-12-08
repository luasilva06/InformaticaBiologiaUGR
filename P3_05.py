''' 5. Crea una lista vacía llamada “plantas”. Utiliza un bucle que pregunte
tres plantas al usuario e inclúyelas en tu lista. Imprime la lista al final. 
Recuerda el uso de la función “append()” '''

# INICIALIZACION

plantas = []

# OPERACIONES

for i in range(3):
    nome = input("Cual es nombre de la planta {}? ".format(i+1))
    plantas.append(nome)

# SALIDAS 

print("La lista de las plantas es: \n{}".format(plantas))