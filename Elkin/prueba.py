from math import pi

class Areas():
    def AreaTriangulo(b,h):
        return (b*h)/2

    print("Area de un triangulo")
    b = float(input('Ingrese la base : '))
    h = float(input('Ingrese la altura : '))

    print("El area del triangulo es:",AreaTriangulo(b,h))


    def AreaCuadrado(b,h):
        return b*h

    print("Area de un cuadrado")
    b = float(input('Ingrese la base : '))
    h = float(input('Ingrese la altura : '))

    print("El area del cuadrado es:",AreaCuadrado(b,h))

    def AreaCirculo(r):
        return round(pi * r ** 2,1)

    print("Area de un circulo")
    r = float(input("Ingrese el radio del circulo: "))
    print("El area del cieculo es ",((AreaCirculo)(r)))
    
