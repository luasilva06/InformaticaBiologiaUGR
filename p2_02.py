'''2. Sustituye todas las apariciones del carácter ‘s’ de una palabra por el símbolo ‘$’. Por ejemplo, 
la palabra “soluciones” quedaría como “$olucione$”.'''

#INICIALIZACION

palabra = input("Cual es la palabra? ")

#OPERACIONES
palabra = palabra.replace("s","$")
#SALIDAS
print("Cambiando 's' por '$': {}".format(palabra))
