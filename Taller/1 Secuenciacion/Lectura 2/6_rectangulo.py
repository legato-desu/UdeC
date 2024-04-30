# Calcule perimetro y superficie de un rectangulo
"""
Elaborar un algoritmo talque dado como datos la base y la 
altura  de un rectángulo, que calcule e imprima su 
perímetro y su superficie 
"""
# Se piden la base y altura de tipo deciaml (float) por teclado
b = float(input('Ingrese la base de el rectangulo: '))
h = float(input('Ingrese la altura de el rectangulo: '))

# Se guarda en las variables las operaciones de cada funcion
perimetro = 2*h + 2*b
superficie = b * h


# El mensaje por pantalla tendra un formato (fstring)

print(f"El perimetro de el rectangulo es: {perimetro}")
print(f"La superficie de el rectangulo es: {superficie}")