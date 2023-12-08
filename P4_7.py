'''
7. Última vuelta de tuerca: queremos dar como salida solamente los kmers más 
frecuentes calculados en el paso anterior. Para ello, debemos seguir los 
siguientes pasos:
a. Saber cuál es el valor que más se repite. Utiliza la función “max”
integrada en Python sobre los valores del diccionario (nota: frecuencias.values())
b. Crea una lista vacía llamada “palabras”. Ahora, recorre todas las
claves (kmers) de tu diccionario y comprueba si su valor es igual al máximo 
(apartado anterior 7.a). En caso afirmativo, añade el kmer a la lista “palabras”
 '''
 # INICIALIZACION

frecuencias = {}
palabras = []
genoma = "CGATATATCCATAG"
k = int(input("Cual es valor de k? "))

# OPERACIONES

## 7.A
for i in range(len(genoma)):
    if len(genoma[i:i+k]) == k:
        frecuencias[genoma[i:i+k]] = 0
    
for i in range(len(genoma)):
    if len(genoma[i:i+k]) == k:
        frecuencias[genoma[i:i+k]] +=1
        
maxiCla = max(frecuencias, key=frecuencias.get)
maxiVal = frecuencias[maxiCla]

## 7.B

for k in frecuencias.values():
    if k == maxiVal:
        palabras.append(k)

print("El dicionario: {}".format(frecuencias))
print("El kmen que más tiene es {} con {} .".format(maxiCla,maxiVal))
print("7.B {}".format(palabras))

