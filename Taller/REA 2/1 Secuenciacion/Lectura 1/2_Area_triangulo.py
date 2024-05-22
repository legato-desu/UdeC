# Calcula area de un triangulo 
"""
Elaborar un algoritmo para calcular el área de un triángulo.  
Se requiere imprimir como salida el área del triángulo.  
Los datos disponibles para lectura son la base y la altura del triángulo.
"""

print(" *** ___   CALUCLA AREA DE TRIANGULO  ___ ***\n")

# Se piden la b y h de tipo deciaml (float) por teclado
b = float(input('Ingrese la base : '))
h = float(input('Ingrese la altura : '))

# Se guarda en la variable (area) el resultado de la operacion
area = (b * h) / 2

""" 
El mensaje por pantalla tendra un formato (fstring) para 
dar formato al texto
"""
print(f"El area del triangulo es: {area}")