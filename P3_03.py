'''Crea un programa que convierta notas numéricas en etiquetas. Así, las notas de 0.0 a 5.0 (no 
inclusive) serán calificadas como “Suspenso”, de 5.0 (inclusive) a 7.0 (no inclusive) aprobado, 
de 7.0 a 9 (no inclusive) notable, y de 9 a 10 sobresaliente. Nota: ¡Es importante que apliques 
bien el orden de comprobación de rangos! No te preocupes a priori por las notas erróneas'''

# INICIALIZACION

nota = float(input("Cual es la nota del alumno? "))

# OPERACIONES & SALIDAS
if (nota <= 0) or (nota < 5) :
    print("Suspenso")
elif (nota >= 5) and (nota < 7):
    print("Aprobado")
elif (nota >= 7) and (nota < 9):
    print("Notable")
elif (nota >= 9) and (nota <= 10):
    print("Sobresaliente")
else:
    print("Nota invalida")
