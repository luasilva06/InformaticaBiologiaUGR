''' Escribe en un comentario del código cuál es el 2-mer más frecuente de la 
cadena GATCCAGATCCCCATAC. Lo que queremos ahora ampliar el ejercicio anterior,
 y buscar los kmers más frecuentes para un valor determinado de “k”.
 Por ejemplo, la siguiente cadena CGATATATCCATAG para k = 3 contiene: 
ATA --> 3 ATC --> 1 CAT --> 1 CCA --> 1 CGA --> 1 GAT --> 1
TAT --> 2 TCC --> 1 TAG --> 1'''

#INICIALIZACION 

genoma = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

k = int(input("Cual es el valor desejado de K? "))

lista = [] 
 
# OPERACIONES

for i in range(len(genoma)):
    if len(genoma[i:i+k]) == k:
        lista.append(genoma[i:i+k])
        

cATA = lista.count("ATA")
cATC = lista.count("ATC")
cCAT = lista.count("CAT")
cCCA = lista.count("CCA")
cCGA = lista.count("CGA")
cGAT = lista.count("GAT")
cTAT = lista.count("TAT")
cTCC = lista.count("TCC")
cTAG = lista.count("TAG") 

# SALIDAS
print(lista)
print("ATA -> {}".format(cATA))
print("ATC -> {}".format(cATC))
print("CAT -> {}".format(cCAT))
print("CCA -> {}".format(cCCA))
print("CGA -> {}".format(cCGA))
print("GAT -> {}".format(cGAT))
print("TCC -> {}".format(cTCC))
print("TAG -> {}".format(cTAG))
