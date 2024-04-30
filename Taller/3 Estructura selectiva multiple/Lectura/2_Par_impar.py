# Dice numero par o impar entre 0 y 9
"""
Elaborar un algoritmo que lea un número entero entre 0 y 9  e 
imprima  el número y si es par o impar. 
"""

# Se piden el numero de tipo entero (int) por teclado
numero = int(input('Ingresa un numero entre 0 y 9: '))

"""
Con el bucle if se ejecuara una operacion anidada con el fin de 
ver si el numero tiene como modulador el cero (0) de ser asi
el numero por teclado sera par, si el modulador no es cero (0) 
sera un numero impar
"""
if (numero % 2) == 0:
    
    # Se da formato al mensaje por pantalla con fstring
    print(f"El numero {numero} es par")
else:
    
    # Se da formato al mensaje por pantalla con fstring
    print(f"El numero {numero} es impar")