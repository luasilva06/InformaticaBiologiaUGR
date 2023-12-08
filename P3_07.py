'''7. Asigna una frase (cadena de texto) a una variable dada. Ahora vamos a
elimina el carácter “a” de la frase imprimiendo en su lugar la “@”. Mezcla las 
órdenes “for” e “if/else” para este propósito. Para evitar el salto de línea
en print, utiliza print(“mensaje”, end=””). Prueba a reemplazar no solo la “a”
sino también toda aparición de la mayúscula “A”.
'''
# INICIALIZACION

texto = input("Cual es la frase? ")

# OPERACIONES & SALIDAS

for i in texto:
    if (i == "a") or (i == "A"):
        print("@",end="")
    else:
        print (i,end="")
        

