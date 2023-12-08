'''2. Escriba un script en Python que lea tres enteros desde teclado y nos diga si están ordenados 
(da igual si es de forma ascendente o descendente) o no lo están. Por ejemplo, la sucesión de 
números 3, 6, 9 estaría ordenada, así como la serie 13, 2, 1 pero no lo estaría la serie 3, 9, 5.
Pista: prueba a usar condicionales “anidados'''

#INICIALIZACION

num1 = int(input("Cual es el primero numero? "))
num2 = int(input("Cual es el segundo numero? "))
num3 = int(input("Cual es el tercero numero? "))

#OPERACIONES & SALIDAS

if ((num1 < num2) and (num2 < num3))  or ((num1 > num2) and (num2 > num3)):
    print("Los valores estan ordenados: {} , {} , {}".format(num1,num2,num3))
    
else:
    print("Los valores NO estan ordenados: {} , {} , {}".format(num1,num2,num3))