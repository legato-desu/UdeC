# Calcula area y volumen de un cilindro
"""
Elaborar un algoritmo talque dado como datos el radio y la 
altura de un cilindro. Que calcule e imprima el área y su volumen.
"""
# Se trae de la libreria math a (pi)
from math import pi

# Se piden el radio y altura de tipo deciaml (float) por teclado
radio = float(input('Ingrese el radio del cilindro: '))
altura = float(input('Ingrese la altura del cilindro: '))

# Se guarda en la variable (area y volumen) el resultado de la operacion
area = 2 * pi * radio * altura
volumen = 2*pi * radio*(radio+altura)


""" 
El mensaje por pantalla tendra un formato (fstring) para 
limitar los decimales a tres (3)
"""
print(f"El area del cilindro es: {area:3f}")
print(f"El volumen del cilinndro es: {volumen:3f}")