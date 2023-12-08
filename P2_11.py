"""3. Chequea el siguiente código que muestra el ejemplo de un inventario para un juego de arcade:
 [...]
 
Ahora haz los siguientes cambios:
a. Añade una nueva clave al inventario que se llame “bolsillo” y que sea una lista que
contenga “concha”, “baya extraña” y “pelusa”. Pista: los nuevos elementos se añaden
“solos”, simplemente hay que “nombrarlos”.
b. Ordena los elementos que tienes en la “mochila”. Pista: usa una función llamada “sort”
c. Por último, elimina el objeto “daga” de la mochila e incrementa en 50 la cantidad de oro. """

inventario = {
 "oro" : 500,
 "bolsa" : ["yesca", "cuerda", "gema"], # Asigna nueva lista a la clave 'bolsa'
 "mochila" : ["xilofono","daga", "saco de dormir","trozo de pan"]
}
# Añade una clave ‘bolsa tela’ y asignar una lista a la misma
inventario["bolsa tela"] = ["manza", "rubi", "perezoso"]
# Ordena la lista que hay en la clave ‘bolsa’
inventario["bolsa"].sort()


#ALTERACIONES

#ITEM A
inventario["bolsillo"] = ["concha","baya extraña","pelusa"]

print("\n {} \n".format(inventario))

#ITEM B

inventario["mochila"].sort()

#ITEM C

print(inventario["mochila"])


eliminacion = inventario["mochila"]

del eliminacion[eliminacion.index("daga")]


print("\n {} \n".format(inventario))

print("\n {} \n".format(inventario))

inventario["oro"] = inventario["oro"] + 50

print("\n {} \n".format(inventario))
