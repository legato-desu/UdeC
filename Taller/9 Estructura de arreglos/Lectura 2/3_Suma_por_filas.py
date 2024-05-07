# Suma por filas
"""
Elaborar un algoritmo que lea números enteros para una matriz  
de 5 x 6, que imprima los elementos de la matriz y que al final de 
cada fila imprima la suma  de todos sus elementos. 
"""

"""
Importamos la libreia numpy para analisis gran voumen numerico y 
acortamos su nombre a np (numpy == np)
"""
import numpy as np

# Creamos la matriz con (zeros) que hace referencia a la dimension del array
matriz = np.zeros((5, 6), dtype=int)

# Llenar matriz
for i in range(5):  # Filas
    for j in range(6):  # Columnas
        
        # Se pide por pantalla los datos para llenar la matriz
        matriz[i, j] = int(input(f"Ingrese F{i+1} C{j+1}: "))

# Imprimir matriz
print(matriz)

# sumar fila con len para ir dato a dato en el array
for i in range(len(matriz)):
    
    # Varible fila almacena los datos de la suma
    fila = sum(matriz[i])
    
    # Con fstring se da formato al mensaje
    print(f"La suma de la fila {i+1} es {fila}")