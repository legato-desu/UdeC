# Tabla de funciones trigonometricas 
"""
Elaborar un algoritmo que imprima el valor del seno, coseno y 
arcotangente de X; para valores de X desde -1 hasta 1 con intervalos de 
0.2. Debe imprimir la siguiente tabla.

    X       SENOX       COSENOX       ARCOTANGENTEX
    
    _______________________________________________
    
    -1.0    99.99        99.99           99.99
    -0.8    99.99        99.99           99.99
    .
    .
    .
    1.0     99.99        99.99           99.99

"""

# Uso de biblioteca math para traer seno, coseno y tangente
import math


# Creamos una funcion para dar formato a la tabla

def Tabla():
    print("X\t\tSENOX\t\tCOSENOX\t\tARCOTANGENTEX")
    print("-" * 60)
    
    """
    Con el buble for daremos un rango de (-5 a 6) pero ese valor lo vamos 
    a multiplicar por 0.2 para ir por decimas de -1 a 1
    """
    for x in [i * 0.2 for i in range(-5, 6)]:
        
        # Guardamos valores de seno coseno y arcotangente en forma ciclica        
        senx = math.sin(x)
        cosx = math.cos(x)
        arcotangentex = math.atan(x)
        
        """
        Con fstring damos formato a la pantalla y con (\t) ajustamos el texto
        y limitamos a 1 decimal 
        """
        print(f"{x:.1f}\t\t{senx:.1f}\t\t{cosx:.1f}\t\t{arcotangentex:.1f}")

Tabla()