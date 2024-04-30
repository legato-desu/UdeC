# Conversor dias a segundos
"""
Elaborar un algoritmo  que calcule e imprima el número de 
segundos que hay en un determinado número de días. 
"""

# Se piden los dias de tipo entero (int) por teclado
dias = int(input('Ingrese la cantidad de dias: '))

# Se guarda en la variable (Segundos) el resultado de la operacion
segundos = dias * 60 * 60 * 24

""" 
El mensaje por pantalla tendra un formato (fstring) para
dar formato y a segundos se agrega puntuacion de centenas
"""
print(f"{dias} dias tienen un totas de {segundos:,} segundos")