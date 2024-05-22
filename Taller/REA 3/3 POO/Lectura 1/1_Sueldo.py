# Calcula sueldo empleado
"""
Elaborar un algoritmo que permita calcular el sueldo de un empleado, 
conociendo su nombre, número de horas trabajadas y valor de hora trabajada. 
El algoritmo debe imprimir el nombre y el sueldo. Utilizar POO. 
"""

# Se crea la clase que almacenara los datos del usuario
class Empleado:
    def __init__(self, nombre, horas_trabajadas, valor_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    # El metodo sueldo dara el retorno de la funcion
    def sueldo(self):
        sueldo = self.horas_trabajadas * self.valor_hora
        return sueldo

    # El metodo salida dara el mensaje por pantalla con un formato legible
    def salida(self):
        sueldo = self.sueldo()
        print(f"Empleado: {self.nombre}\nSueldo: ${sueldo:,.0f}")


# Se pide al usuario el nombre de modo string
nombre_empleado = input("Ingrese el nombre del empleado: ")

# Se da un capitalize para dar mayuscula al nombre
nombre_empleado = nombre_empleado.capitalize()

# Se pide la hora y su valor con formato float
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de la hora trabajada: "))

# Se hace la interaccion con la clase y sus metodos
empleado = Empleado(nombre_empleado, horas_trabajadas, valor_hora)
empleado.salida()