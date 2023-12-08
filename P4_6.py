'''6. Implementa un código que resuelva el problema de generar el mapa de 
frecuencia para un k determinado. No desesperes, te guiaremos en la tarea.

a. En primer lugar, crea un diccionario vacío: frecuencias = {}
b. Recorre todo el texto haciendo “slicing” para el valor k y guarda como 
clave cada kmer y como valor un 0. 
c. Ahora actualiza la asignación directa para el valor 0 que hiciste 
anteriormente. Como pista, piensa que si el kmer está ya en tu diccionario 
de frecuencias debes sumarle uno, en lugar de asignarle un 0. 
Nota: para saber si un elemento está en un diccionario utiliza la orden “if” 
como “clave in diccionario”
d. Prueba tu programa con los valores que indicamos antes: CGATATATCCATAG, k = 3'''

# INICIALIZACION

frecuencias = {}
genoma = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = int(input("Cual es valor de k? "))

# OPERACIONES

for i in range(len(genoma)):
    if len(genoma[i:i+k]) == k:
        frecuencias[genoma[i:i+k]] = 0
    
for i in range(len(genoma)):
    if len(genoma[i:i+k]) == k:
        frecuencias[genoma[i:i+k]] +=1


# SALIDAS    
print(frecuencias)