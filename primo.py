'''Pedir um valor e saber se é primo'''
 # OPERACIONES 
num = int(input("Cual es numero? "))
div = 0

for i in range(1,num+1):
    if num%i == 0:
        div +=1

if div == 2:
    print("{} es primo, ya que fue dividido {} veces".format(num,div))
else:
    print("{} no es primo, ya que fue dividido {} veces".format(num,div))
