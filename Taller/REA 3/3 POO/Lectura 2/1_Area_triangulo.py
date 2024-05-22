# Calcula area triangulo
"""
Elaborar un algoritmo para calcular el área  de un triángulo.  
Se requiere imprimir como salida el área del triángulo. 
Los datos disponibles para leer como entrada son la base y la 
altura del triángulo. Utilizar POO. 
"""

# La clase triangulo tendra las palabras clave base y altura por teclado
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # El metodo area tendra la ecuacion para el 
    # triangulo y retornara el resultado
    def area(self):
        area = (self.base * self.altura) / 2
        return area

# Se pide por teclado la base y altura de tipo float 
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

# Se hace el llamado a la clase principal 
triangulo = Triangulo(base, altura)

# Se pide la ecuacion de el metodo
area = triangulo.area()

# Con fstring se da formato al mensaje por pantalla
print(f"El área del triángulo es: {area}")