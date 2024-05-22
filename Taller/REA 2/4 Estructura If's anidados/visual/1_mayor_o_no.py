# Mayor de edad o no
"""
Escribir un programa que indique si una persona es mayor de edad o no
"""

# Se piden la edad de tipo entero (int) por teclado
edad = int(input('Ingrese la edad de la persona: '))

"""
El bucle if evaluara la edad de ser mayor o igual a 18 
dira que la persona es mayor de no ser asi sera menor de edad
"""
if edad >= 18:
    print('La persona es mayor de edad')
else:
    print('La persona es menor de edad')