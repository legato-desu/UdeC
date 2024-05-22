# Calcula seno y coseno
"""
Elaborar un algoritmo que permita leer el tamaño de un ángulo en 
radianes, que calcule e imprima el valor del seno y del coseno. 
"""

# Se importa la libreria math para el uso de seno y coseno
import math

# La clase angulo obtendra las radianes introducidas por teclado
class Angulo:
    def __init__(self, radianes):
        self.radianes = radianes
    
    # El metodo seno retornara la conversion 
    def seno(self):
        return math.sin(self.radianes)
    
    # El metodo coseno retornara la conversion 
    def coseno(self):
        return math.cos(self.radianes)

# Se pedira por teclado el angulo radial de tipo float
angulo_radianes = float(input("Ingresa el tamaño del ángulo en radianes: "))

# Se hace el llamado a la clase principal
angulo = Angulo(angulo_radianes)

# Se pide la conversion a cada metodo 
seno = angulo.seno()
coseno = angulo.coseno()

# Se muestra por pantalla el resultado de forma legible 
print(f"El seno del angulo es: {seno:.7f}")
print(f"El coseno del angulo es: {coseno:.7f}")