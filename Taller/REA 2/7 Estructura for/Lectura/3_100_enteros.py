# Suma los primeros 100 numeros enteros
"""
Elabora un algoritmo que calcule e imprima la suma de los
numeros enteros del 1 al 100

Analisis del problema:
1+2+3+4+5+....100=?

1+2+3+4+5+.....100 = n(n+1)/2  (Serie de Gauss)

si n = 2

2(2+1)/2 = 3

Si n=4

4(4+1)/2 = 10
"""

""""
se inicia el bucle fer con el valor cambiante de (i) en un rango de 100
numeros
"""
for i in range (101):
    
    """
    En la variable suma haremos el procedimiento gauss sabiendo que i 
    tendra un aumento hasta llegar a 100
    """
    suma = i * (i + 1)/ 2

"""
El fstring estara fuera del bucle para lanzar el ultimo valor de la
variable suma asi se enseñara solo el resultado de el acumulado de la ultima
operacion y se eliminara el decimal 
"""
print(f"{suma:.0f}")