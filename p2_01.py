'''1. Crear 3 variables de tipo “string” (cadena de texto) con el contenido que quieras. A 
continuación, probar lo siguiente:
a. Imprime las 3 variables con 3 sentencias “print” diferentes. 
b. Imprime las 3 variables en una única sentencia print como: “Cadena1: 
<contenido1>, Cadena2: <contenido2>, Cadena3: <contenido3>” 
donde contenido1, contenido2, y contenido3 es el valor asignado a cada cadena. 
c. Imprime la primera letra de la primera cadena, después la cuarta letra de la segunda 
cadena y luego la última letra de la tercera cadena. Pista: [ ? ]
d. Imprime las tres cadenas anteriores todas en mayúsculas. Pista: funciones de string.
e. Por último, imprime la longitud de cada una de las tres cadenas anteriores'''

#INICIALIZACION
cadena01 = input("Cual es la 1ª cadena? ")
cadena02 = input("Cual es la 2ª cadena? ")
cadena03= input("Cual es la 3ª cadena? ")


# SALIDAS
print("\n1.a -> \n")
print(cadena01)
print(cadena02)
print(cadena03)


print("\n 1.b -> \n")
print("Cadena 1: {}, cadena 2: {}, cadena 3: {}".format(cadena01,cadena02,cadena03 ))

salida = cadena01[0] + cadena02[3] + cadena03[-1]

print("\n 1.c -> \n")
print(salida)

cadena01 = cadena01.upper()
cadena02 = cadena02.upper()
cadena03 = cadena03.upper()

print("\n 1.d -> \n")
print("Cadena 1: {}, cadena 2: {}, cadena 3: {}".format(cadena01,cadena02,cadena03))

print("\n 1.e -> \n")
print("longitude cadena 1: {}, cadena 2: {}, cadena 3: {}".format(len(cadena01),len(cadena02),len(cadena03) ))
