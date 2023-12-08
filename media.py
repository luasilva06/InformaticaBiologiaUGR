'''Realizar um programa que peça 10 valores  e devolver a media'''

#INICIALIZACION

num = 0

# OPERACIONES

for i in range(10):
    num = int(input("Cual es el valor {} ?".format(i+1)))
    num += num
    
# SALIDAS 

print("La media de los valores es: {}".format(num/10))
