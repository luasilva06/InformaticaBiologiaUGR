'''10. Prueba el siguiente código y comprueba el uso de la orden ”enumerate”.
Fíjate cómo permite utilizar un índice para llevar la cuenta de los elementos. 
Haz que el índice empiece mostrándose en 1, como es natural.
opciones = ['pizza', 'pasta', 'ensalada', 'nachos']
print('Tus opciones son:')
for index, item in enumerate(opciones):
 print (index, item)'''
 
 # INICIALIZACION
 
opciones = ["pizza", "pasta", "ensalada", "nachos"]

# OPERACIONES & SALIDAS

print("Tus opciones son:")
for index, item in enumerate(opciones):
    print(index+1,item)