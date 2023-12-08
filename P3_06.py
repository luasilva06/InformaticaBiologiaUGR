'''6. Define una variable como una cadena de texto. Utiliza un bucle “for” para
imprimirla carácter a carácter. NO utilices la función “range()”,
usa la propia variable como “iterable”'''

# INICIALIZACION

cad = input ("Cual es el texto? ")
inde = 1
# OPERACIONES & SALIDAS

for i in cad:
    print("El caracter en la posicion {} es {}".format(inde,i))
    inde += 1