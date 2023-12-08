'''1. Escribe una sentencia “if” para comprobar si una subcadena está en un 
texto mayor, y en caso afirmativo que sume 1 a un contador. En concreto, 
dados kmer = “ATA” y genoma = “CGATATATCCATAG” crea una orden que pueda 
comparar a partir de cualquier posición i-ésima del genoma, es decir, 
no uses valores absolutos si no relativos (variables).'''

# INICIALIZACION
kmer = "ATA"
genoma = "CGATATATCCATA"

contador = 0

# PROCEDIMIENTOS 
for i in range(len(genoma)):
    if kmer == genoma[i:i+3]:
        contador +=1

# SALIDA
print ("la secuencia aparece {} veces".format(contador))