# Calcula seno y coseno
"""
Elaborar un algoritmo que permita leer el tamaño de un ángulo 
en radianes, luego que calcule e imprima el valor del seno y del coseno 
"""
# Se importa la libreria math para usar seno (sin) y coseno (cos)
import math

# Se piden el angulo en radianes de tipo deciaml (float) por teclado
angulo = float(input('Ingrese el tamaño del angulo (en radianes): '))

# Con ayuda de la libreria usamos los valores de sin y cos para los angulos
seno = math.sin(angulo)
coseno = math.cos(angulo)

""" 
El mensaje por pantalla tendra un formato (fstring) para
limitar los decimales a cuatro (4)
"""
print(f"El valor de seno es: {seno:.4f}")
print(f"El valor de coseno es: {coseno:.4f}")
