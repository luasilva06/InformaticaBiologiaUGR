'''3. Combina el ejercicio 1 dentro de un bucle que funcione como una ventana 
deslizante. Prueba con genoma GCGCG y el kmer GCG;
la salida debería ser igual a 2.'''

# INICIALIZACION
kmer = "GCG"
genoma = "GCGCG"

contador = 0
ventana = 3

# PROCEDIMIENTOS 
for i in range(len(genoma)-ventana+1):
    print("Fragmiento de genoma: {}".format(genoma[i:i+ventana]))
    if kmer == genoma[i:i+ventana]:
        contador +=1
       
        

# SALIDA
print ("la secuencia aparece {} veces".format(contador))
