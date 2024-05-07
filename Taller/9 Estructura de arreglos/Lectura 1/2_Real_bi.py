# Captura e imprime numeros reales en arreglo bidimensional
"""
Elaborar un algoritmo que capture números reales en una matriz 
de 3x4  y que lo imprima
"""

"""
Importamos la libreia numpy para analisis gran voumen numerico y 
acortamos su nombre a np (numpy == np)
"""
import numpy as np

# Creamos la matriz con (zeros) que hace referencia a la dimension del array
matriz = np.zeros((3, 4), dtype=float)

# Llenar matriz
for i in range(3):  # Filas
    for j in range(4):  # Columnas
        
        # Se piden los datos por pantalla y se guardan de tipo reales
        matriz[i, j] = float(input(f"Ingrese F{i+1 } C{j+1}: "))

# Imprimir matriz
print(matriz)