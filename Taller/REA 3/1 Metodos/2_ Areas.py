# Calcula areas de figuras geometricas
"""
Elaborar un algoritmo que ofrezca un menú de opciones, mediante el cual
se pueda escoger calcular el área de las figuras geométricas: 
triangulo, cuadrado, rectángulo y circulo. 
Una vez seleccionada la opción, que llame a un método que permita solicitar y 
leer los datos necesarios, hacer el calculo correspondiente e imprimirlo. 

AREAS DE FIGURAS GEOMETRICAS
1: TRIANGULO
2: CUADRADO
3: RECTANGULO
4: CIRCULO
5: FIN
OPCION: 
"""

# Se importa la libreria math para dar uso al numero pi
from math import pi

# Se crea la clase que contendra los datos por teclado
class Areas:

    """
    Se crearan los metodos correspondientes a las diferentes 
    areas del menu y cada una de ella retornara su respectivo resultado
    segun su formula base
    """
    def triangulo(self,b,h):
        return (b * h) / 2

    def cuadrado(self,l):
        return l * l
    
    def rectangulo(self,b,h):
        return b * h
    
    def circulo(self,r):
        return (r**2)*pi 

# El metodo menu tendra el despliegue de la tabla de contenidos a elegir 
def menu():
    print("AREAS DE FIGURAS GEOMETRICAS: \n \
    1: TRIANGULO\n \
    2: CUADRADO\n \
    3: RECTANGULO\n \
    4: CIRCULO\n \
    5: FIN")
    
# area tendra como argumento el llamado de los metodos areas
area = Areas()

"""
El bucle while se iniciara de forma automatica dando asi el despliegue 
de menu y tras eso almacenando la opcion elejida 
"""
while True:
    menu()
    opcion = int(input("Opcion: "))
        
    """
    Los bucles if llevaran consigo las funciones de cada opcion del 
    menu
    """
    if opcion == 5:
        
        """
        En caso tal de recibir el argumento Fin se dara un break
        para finalizar el programa
        """
        print("Programa finalizado")
        break
    
    # Se inica el ciclo if para el area de triangulo
    if opcion == 1:
        
        # Se da un texto informativo con la ecuacion por pantalla
        print("\t*** AREA DE UN TRIANGULO ***")
        print("\t\tA = b * h\n \
        \t      2")
        
        # Las variables almacenaran base y altura de tipo float
        base = float(input("Ingrese base: "))
        altura = float(input("Ingrese altura: "))
        
        # Se da por pantalla su respectiva area
        print(f"El area del triangulo es: {area.triangulo(base,altura):.0f}(cm)^2")
        
        # Se hace una pausa en pantalla
        fin=input()

    # Se inica el ciclo if para el area de cuadrado
    if opcion == 2:
        
        # Se da un texto informativo con la ecuacion por pantalla
        print("\t*** AREA DE UN CUADRADO ***")
        print("\t\tA = L * L")
        
        # Las variables almacenaran el lado de tipo float
        lado = float(input("Ingrese un lado: "))
        
        # Se da por pantalla su respectiva area
        print(f"El area del cuadrado es: {area.cuadrado(lado):.0f}(cm)^2")
    
        # Se hace una pausa en pantalla
        fin = input()
        
    # Se inica el ciclo if para el area de un rectangulo
    if opcion == 3:

        # Se da un texto informativo con la ecuacion por pantalla
        print("\t*** AREA DE UN RECTANGULO ***")
        print("\t\tA = b * h")
        
        # Las variables almacenaran base y altura de tipo float
        altura = float(input("ingrese altura: "))
        base = float(input("Ingrese base: "))
        
        # Se da por pantalla su respectiva area
        print(f"El area del rectangulo es: {area.rectangulo(base,altura):.0f}(cm)^2")
        
        # Se hace una pausa en pantalla
        fin = input()

    # Se inica el ciclo if para el area de circulo
    if opcion == 4:
        
        # Se da un texto informativo con la ecuacion por pantalla
        print("\t*** AREA DE UN CIRCULO ***")
        print("\t\tA = π * r^2")
        
        # Las variables almacenaran radio de tipo float
        radio = float(input("Ingrese radio: "))
        
        # Se da por pantalla su respectiva area
        print(f"El area del circulo es: {area.circulo(radio):.2f}(cm)^2")
        
        # Se hace una pausa en pantalla
        fin = input()