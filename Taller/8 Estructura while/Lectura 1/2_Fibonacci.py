# Calcula el numero 180 de la serie de fibonacci
"""
Elaborar un algoritmo que calcule el término 180 de la Serie de Fibonacci. 
Recuerde que los dos primeros números de la serie  son 0 y 1,
los demás se obtienen como la suma de los números inmediatos que le preceden. 
0,1, 1,2, 3, 5,8,13, ……, 
"""

# Se crea una funcion de fibonacci para tener el valor de num
def fibonacci(num):
    
    # Inicializamos 2 variables para hacer la secuecia de incremento en bucle
    a,b = 0,1
    
    # El bucle for hara n veces el valor segun num 
    for i in range(num):
        
        # Se crea el ciclo para hacer la formula fibonnaci
        c = b+a
        a = b
        b = c
        
    return a

# Se imprime el termino segun su funcion en parentesis ()
print(fibonacci(180))