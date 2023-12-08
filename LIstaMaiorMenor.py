# -*- coding: utf-8 -*-
"""
Qual o maior valor e a sua posição de uma lista? 
o ruim de usar o index é que ele só mostra um valor, se tiver varios valores iguais ele falha
"""

lista = [2,4,5,6,1,-1,4,10,10]
maximo = lista[0]
minimo = lista[0]
posiMax = 0
posiMin = 0

for i in range(len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
        posiMax = i
    if lista[i] < minimo:
        minimo = lista[i]
        posiMin = i
        
print("El mayor es {} y su posicion es {}".format(maximo,posiMax))
print("El menor valor es {} y su posicion es {}".format(minimo,posiMin))
