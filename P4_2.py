'''2. Escribe en un comentario de código en qué posición deberemos parar la 
búsqueda de una ventana de 10 nucleótidos en un genoma de longitud 1000. Esto 
te indicará dónde empieza el último “kmer” que busques en tu cadena 
de ADN original. Pista: fíjate en el gráfico anterior.'''


genoma= input("Cual es genoma de tamaño 1000?")
ultiKMER = 0
ventana = int(input("Cual es tamaño de la ventana? "))
   
print(genoma[-ventana:])

    
    
        