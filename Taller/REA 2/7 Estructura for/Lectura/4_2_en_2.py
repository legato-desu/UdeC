# Suma los numeros pares del 2 al 160

"""
Elabora un algoritmo que calcule e imprima la suma de los numeros 
pares del 2 hasta el 160

Analisis del problema:

2+4+6+8+.....+160 = ?
"""

# Iniciamos una constante en cero(0)

suma = 0

"""
En el bucle for se hara un rango de los numeros de 0 a 162 guardando en i
los numeros pares 
"""
for i in range (0,162,2):
    
    """
    suma tendra el valor ciclico de i y se sumara consigo mismo hasta que 
    llegue a 160 dando fin al bucle
    """
    suma = suma + i

# Con fstring se enseñara la ultima suma almacenada en la variable 
print(f"{suma:.0f}")