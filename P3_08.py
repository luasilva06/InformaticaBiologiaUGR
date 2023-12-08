'''8. Construye una lista con al menos 5 números diferentes.
Crea un bucle para imprimir los cuadrados de todos los números de tu lista.
'''
# INICIALIZACION
lista = []
for i in range(5):
        num = int(input("cual es numero que quieres añadir? "))
        lista.append(num)
print(lista)

# OPERACIONES & SALIDAS 

for j in range(5):
    cuad = lista[j] ** 2
    print("lo cuadrado de {} es {}".format(lista[j],cuad))