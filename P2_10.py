'''2. Crea una variable de tipo diccionario que contenga un menú (dale dicho nombre).
Considera los siguientes
a. Las claves serán los nombres de los platos, y el valor será su precio.
b. Añade al menos 4 platos, imprime primero el número de elementos de tu menú y
continuación imprime la variable “menu”.
c. Cambia el precio de uno de tus artículos.
d. Por último, elimina uno de los platos “menos populares” (a tu elección). 
'''
#INICIALIZACION

menu = {}

#OPERACIONES

# Anadindo los platos al diccionario
plato = input("¿Cual es el nombre del plato que desea anadir al menù?")
precio = float (input("¿Cual es el precio de ese plato?"))
menu[plato] = precio

plato = input("¿Cual es el nombre del plato que desea anadir al menù?")
precio = float (input("¿Cual es el precio de ese plato?"))
menu[plato] = precio

plato = input("¿Cual es el nombre del plato que desea anadir al menù?")
precio = float (input("¿Cual es el precio de ese plato?"))
menu[plato] = precio

plato = input("¿Cual es el nombre del plato que desea anadir al menù?")
precio = float (input("¿Cual es el precio de ese plato?"))
menu[plato] = precio

# Salidas del item B

tamano = len(menu)

print("El menù tiene {} elementos".format(tamano))
print(menu)

# ITEM C
plato = input("¿Cual es el nombre del plato que desea TENER EL PRECIO CAMBIADO?")
precio = float (input("¿Cual es el NUEVO PRECIO del PLATO?"))

print("/nMENU ACTUALIZADO /n{}".format(menu))

#ITEM D
plato = input("¿Cual es el nombre del plato MENOS POPULAR que desea eliminar?")
del menu[plato]

print("/nMENU ACTUALIZADO /n{}".format(menu))
