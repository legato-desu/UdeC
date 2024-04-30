# Area y Perimetro
"""
Crea un programa que calcule el area y el perimetro de un 
rectangulo tras ingresar la base y la altura por el usuario 

Formulas:
    area = b x h 
    perimetro = 2 x (b + h)
    
    donde:
    b = base y h = altura
"""

print('Calculo del area y perimetro de un rectangulo')

# Se piden la base y altura de tipo decimal (float) por teclado
b = float(input('Ingrese la base: '))
h = float(input('Ingrese la altura: '))

# Se guarda en la variable (area y perimetro) el resultado de la operacion
area = b*h
perimetro = 2*(b+h)

""" 
El mensaje por pantalla tendra un formato (fstring) para
limitar los decimales a cero (0) y dos (2)
"""
print(f"El area del rectangulo es: {area:.0f} (m)^2")
print(f"El perimetro del rectangulo es {perimetro:.2f} cm")