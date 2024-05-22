# Calcula promedio estudiante
"""
Elaborar un algoritmo para calcular el promedio de calificaciones de un 
estudiante. Los datos disponibles para lectura son el nombre del 
estudiantes, calificación 1, calificación 2 y calificación 3, 
de cada uno de los tres exámenes presentados. 
La información que se debe imprimir  es el nombre del estudiante y el 
promedio de calificaciones. Utilizar POO. 
"""

# La clase estudiante almacenara las variables por teclado 
class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    # El metodo promedio retornara el calculo pedido
    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

# Función para solicitar datos de un estudiante
def datos_estudiante():
    
    # Se pide el nombre de tipo string
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Capitalizamos nombre para dara formato
    nombre = nombre.capitalize()
    
    # Se piden las notas de tipo float
    nota1 = float(input("Ingrese la calificación 1: "))
    nota2 = float(input("Ingrese la calificación 2: "))
    nota3 = float(input("Ingrese la calificación 3: "))
    
    # Se retorna cada dato almacenado por teclado
    return Estudiante(nombre, nota1, nota2, nota3)

# Función principal
def main():
    
    # Se hace el llamado de cada metodo 
    estudiante = datos_estudiante()
    promedio = estudiante.promedio()
    
    # Se da un mensaje por pantalla
    print(f"El promedio de {estudiante.nombre} es: {promedio:.1f}")

# Se inicia el metodo principal
main()