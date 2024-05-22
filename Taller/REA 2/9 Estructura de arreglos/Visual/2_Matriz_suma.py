# Suma de matriz bidimensional 
"""
Elabora un programa que lea una matriz 3x4 e imprima su matriz y la
suma de cada fila y columna
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

# sumar fila con len para ir dato a dato en el array
for i in range(len(matriz)):
    
    # La variable fila tendra la suma de cada respectivo numero
    fila = sum(matriz[i])
    
    # Con fstring darmos formato al mensaje por pantalla
    print(f"La suma de la fila {i+1} es {fila}")
    
# sumar columna con len para ir dato a dato en el array
for j in range(len(matriz[-1])):
    
    # Iniciamos la variable suma para guardar la intereacion
    columna = 0
    
    # El for anidado hara el recorrido de la matriz para buscar las columnas
    for i in range(len(matriz)):
        
        # Se suma cada dato de la columna
        columna += matriz[i][j]   
        
    # Con fstring darmos formato al mensaje por pantalla 
    print(f"La suma de la columna {j+1} es {columna}")