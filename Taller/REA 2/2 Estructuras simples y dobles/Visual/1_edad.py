# Edad
"""
Crea un programa para determinar si una persona es mayor de edad
"""

# Se piden la edad de tipo entero (int) por teclado
edad = int(input('Ingrese su edad: '))

# Con el bucle if podemos ver analizar si es mayor de edad o no
if edad >= 18:
    print('Mayor de edad')
else:
    print('Menor de edad')