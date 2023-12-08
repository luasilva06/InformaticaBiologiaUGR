'''4. Dadas dos palabras “string1” y “string2”, crea una frase “string3” como 
unión de las dos anteriores. Por ejemplo, string1 = “hola”, string2 = “mundo”, 
string3 = “hola mundo”. ¡No olvides el espacio intermedio entre ambas!'''

#INICIALIZACION

cadena1 = input("Cual es la 1ª palabra? ")
cadena2 = input("Cual es la 2ª palabra? ")

#OPERACIONES

cadena3 = cadena1+" "+cadena2

#SALIDAS

print("La cadenas '{}' y '{}' fueron concatenadas en una nueva: '{}'".format(cadena1,cadena2,cadena3))