# Conversor de rad-grand y grad-rad
"""
Elaborar un algoritmo que permita leer un número en radianes e 
imprima su equivalencia en grados; asimismo, que permita 
leer un número en grados e imprima su equivalencia en radianes. 
"""

# De la libreria math extraemos solo a (pi)
from math import pi

# Se piden los radianes y grados de tipo deciaml (float) por teclado
radianes = float(input('Ingrese el angulo en radianes: '))
grados = float(input('Ingrese el angulo en grados: '))

# Se guardan las conversines en sus respectivas variables
num_grados = radianes * 180 / pi
num_radianes = grados * pi / 180

""" 
El mensaje por pantalla tendra un formato (fstring) para
limitar los decimales a cuatro (4) y cero (0)
"""
print(f"{radianes:.4f} radianes, equivale a {num_grados:.0f}°")
print(f"{grados:.0f}°, equivale a {num_radianes:.4f} radianes")