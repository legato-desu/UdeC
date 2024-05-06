# Calcula el factorial de un numero
"""
Elaborar un algoritmo que lea un valor N, entero y positivo, y 
que calcule e imprima su factorial. Por ejemplo,  si se lee 5, su 
factorial es el producto de  5*4*3*2*1.  
El factorial de O es 1. Solución: Análisis del problema 5!= 5*4*3*2*1  
0! = 1  
"""

# Se piden numero tipo entero (int) por teclado
num = int(input("Ingrese un numero entero positivo: "))

"""
En el bucle if revisamos que cumpla con los requisitos para porder
hacer el calculo del factorial
"""
if num > 0:
    
    """
    Inicia una variable con uno (1) para poder ejecutar el bucle de forma correcta
    pues si inicia en cero (0) no se hara el incremento de i
    """
    fact = 1
    
    """
    Para dar mejor formato a la pantalla podremos una variable de tipo 
    string en blanco que alacenara un ciclo de variables tipo caracter
    """
    formu = ""
    
    """
    El bucle for iniciara desde 1 hasta n numero (num) dando asi el ciclo
    repetitivo del bucle
    """
    for i in range (1,num+1):
        
        # factorial = factorial * i (i tendra el rango de el factorial)
        fact *= i
        
        # Se almacena la i pero ahora en modo caracter y se concatena una (x)
        formu = formu + str(i)+"x"
    
    # Se elimina la ultima letra de la cadena almacenada en este caso la (x) final
    formu = formu [:-1]

    # Con fstring se da formato legible al mensaje por pantalla
    print(f"{fact}!={formu}")
    
    """
si el numero ingresado es cero (0) el bucle llegara a esta parte y 
dara por pantalla un valor de 0! = 1
"""
elif num == 0:
    
    # la constante fact tendra un 1 almacenado 
    fact = 1
    
    # Con fstring se da dormato al mensaje
    print(f"{num}! = {fact}")
    
else:
    print("No es un numero entero positivo!")