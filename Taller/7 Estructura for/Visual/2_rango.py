# Con el bucle for imprimir numeros
"""
Crea un programa que enseñe por pantalla un orden incrementado y otro con
decremento de forma simultanea
"""

# Iniciamos directamente el bucle anidado
for i in range(5):
    
    """
    En el primer nido tendremos el rango de (i) pero
    daremos valor a (j) dentro de este primer bucle
    """
    j = 10
    """
    La variable (_) ejecutara el segundo nido para hacer el calculo e imprimir 
    por pantalla los valores de (i) y (j)
    """
    for _ in range(i):
        
        # En (j) se ejeturara una accion con el bucle (i)
        j *= i / 2
        
    # Con fstring enseñamos en pantalla los valores que guardamos en los bucles
    print(f"i:{i} - j:{j}")