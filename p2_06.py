''' 1. Imagina que gestionas un refugio de animales. Crea una lista “animales”
con aquéllos que mantengas en dicho refugio, con al menos 4 tipos diferentes. 
Ahora haz las siguientes tareas:
a. Muestra en pantalla todos los animales de tu lista. 
b. Sustituye un animal cualquiera por un “perezoso”. 
c. Usa la función “index” para encontrar en qué lugar se ha guardado el “perezoso”. 
d. Usa la función “insert” para insertar en esa posición una “pitón”. '''

#INICIALIZACION
animales = []

#OPERACIONES

animales.append(input("Adicione 1º animal a la lista "))
animales.append(input("Adicione 2º animal a la lista "))
animales.append(input("Adicione 3º animal a la lista "))
animales.append(input("Adicione 4º animal a la lista "))

# SALIDAS
print(animales)

#OPERACIONES
perez = int(input("Cual es la posicion del animal que quieres cambiar? 0 a 3: "))
animales[perez] = "Perezoso"

#SALIDA item b

print("\n\t item b")
print("Despues de cambiar el animal la lista ahora es: {}".format(animales))

# OPERACIONES

posic = animales.index("Perezoso")

#SALIDAS
print("\n\t item c")
print("El index de 'Perezoso' es: {}".format(posic))

#OPERACIONES
animales.insert(posic,"Pitón")

#SALIDAS
print("\n\t item d")
print("Despues de cambiar el animal la lista ahora es: {}".format(animales))