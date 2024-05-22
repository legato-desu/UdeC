# Diagonal de un rectangulo
"""
Crea un programa que calcule la diagonal de un rectangulo 
con la base y la altura ingresada por el usuario

Formula:
    D = raiz(b**2 + h**2)
    donde b = base y h = altura
"""
# Se importa la libreria math para sacar raiz cuadrada (sqrt)
import math 

print('Diagonal de un rectangulo')

# Se piden la base y altura de tipo decimal (float) por teclado
b = float(input('Ingrese la base: '))
h = float(input('Ingrese la altura: '))

# Se guarda en la variable (d) el resultado de la operacion
d = math.sqrt(b**2 + h**2) 

""" 
El mensaje por pantalla tendra un formato (fstring) para
limitar los decimales a dos (2)
"""
print(f"La diagonal del rectangulo es: {d:.2f}")