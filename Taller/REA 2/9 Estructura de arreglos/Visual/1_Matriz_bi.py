# Matriz bidimensional
"""
Elabora un programa que lea una matriz 3x4 e imprima su matriz 
"""
"""
Importamos la libreia numpy para analisis gran voumen numerico y 
acortamos su nombre a np (numpy == np)
"""
import numpy as np

# Creamos la matriz con (zeros) que hace referencia a la dimension del array
matriz = np.zeros((3, 4), dtype=int)

# Llenar la matriz con for anidados 
for i in range(3):  # Filas
    for j in range(4):  # Columnas
        
        # Pedimos por pantalla los numeros para la matriz 
        matriz[i, j] = int(input(f"Ingrese F{i+1} C{j+1}: "))

# Imprimir matriz
print(matriz)

fin = input()