'''2. Crea una lista de números, con al menos 4 valores (enteros o reales).
a. Imprime el resultado de sumar el primer valor con el tercero. 
b. Ahora la multiplicación del segundo con el cuarto.'''

#INICIALIZACION

nums = []

#OPERACIONES
nums.append(int(input("Adicione 1º numero a la lista ")))
nums.append(int(input("Adicione 2º numero a la lista ")))
nums.append(int(input("Adicione 3º numero a la lista ")))
nums.append(int(input("Adicione 4º numero a la lista ")))

#OPERACIONES

N1SumN3 = nums[0] + nums[2]
N2MultN4 = nums[1] * nums[3]

#SALIDAS
print("\n La suma del 1º valor ({}) con el 3º ({}) es: {}".format(nums[0],nums[2],N1SumN3))
print("\n La multiplicacion del 2º valor ({}) por el  4º valor ({}) es: {}".format(nums[1],nums[3],N2MultN4))