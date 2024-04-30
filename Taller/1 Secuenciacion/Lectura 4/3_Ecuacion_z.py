# Calcula valor ecuacion z
"""
Elaborar un  algoritmo que lea el valor de W e 
imprima el valor de Z, de la siguiente ecuación 

z = e**w**3  + Ln |w|
    √2 pi w  
"""

# Se importa la libreria math para usaar (pi) y raiz cuadrada(sqrt)
import math
from math import pi, sqrt

print('Z= \n    e**w**3  + Ln |w|\n\
    √2 pi w  ')

# Se pide el valor de (w) por teclado
w = int(input('Ingresa el valor de W (con W > 0 ): '))

# Por el bucle (if) verificamos que no sea un numero negativo
if w > 0:
    
    # Se fragmenta la ecuaciion para llevar un orden
    a = w**3        # w**3
    b = math.exp(a) # e**w**3
    c = 2*pi*w      # 2*pi*w
    d = sqrt(c)     # Raiz 2*pi*w
    f = abs(w)      # |w|
    g = math.log(f) # ln |w|
    z = b/d + g     # e**w**3 / Raiz 2*pi*w + ln |w|
    
    """ 
    El mensaje por pantalla tendra un formato (fstring) para poner puntuacio 
    de centenas y limitar los decimales a dos (2)
    """
    print(f"El valor de z es: {z:,.2f}")
    
# Si (w) es negativo se salta la ecuacion y se lleva al (else)
else:
    print('W debe ser entero positivo')