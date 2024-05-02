# Calcula sueldo varios empleados 
"""
Elabora un algoritmo que calcule e imprima el sueldo de varios empleados,
cada empleado se tratara en forma simimlar al problema de calculo
de sueldo de un empleado

En el problema anterior de sueldos de varios empleados, es necesario 
que los datos se impriman en forma de un reporte que tenga el siguiente formato. 

        REPORTE EMPLEADO
    Nombre                  Sueldo
    ______________________________
    XXXXXX                  999.99
    XXXXXX                  999.99
    -
    -
    -
    XXXXXX                  999.99
    TOTAL 99 EMPLEADOS      9999.99
"""

# Se crea una clase regirstro para procesar el nombre y sueldo de lista
class Registro:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

# Se inician variables en limpio para iniciara bucle y alacenar acumuladores
empleados = 0
salarios = 0
eleccion = 'S'
lista = []

# Se define un (todos) para traer de lista cada dato guardado
def Todos():
    
    # L tendra el punto de origen de el bucle while 
    L = 0
    
    # Con el bucle while procesaremos uno por uno (len) de la lista
    while L < len(lista):
        """
        Con fstring se da formato al mensaje en pantalla con saltos tabulados (\t)
        y una separacion por centanas y cero(decimales)
        """
        print(f"\t\t{lista[L].nombre}\t\t\t${lista[L].sueldo:,.0f}")
        
        # L tendra un aumento de 1 por cada ingreso al bucle hasta que la lista quede en cero
        L += 1
        
"""
El bucle while procesara todo los datos para almacenar en la lista y tambien 
para analizar las formulas 
"""
while eleccion == 'S':
    
        # Se pide el nombre de tipo texto (string) por teclado
        nombre = input("Ingrese el nombre del empleado: ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        nombre =nombre.capitalize()
        
        # Se piden las horas de tipo entero (int) por teclado
        horas = int(input("Horas trabajadas: "))
        
        # Se piden el valor de hora de tipo decimal (float) por teclado
        valor_h = float(input("Valor de horas trabajadas: "))

        # En la variabe sueldo guardaremos la operacion con redondeo de decimales
        sueldo = round(horas * valor_h)
        
        # En las variables empleados y salarios se hara un incremento para almacenar
        empleados = empleados + 1
        salarios = salarios + sueldo
    
        # Guardaremos en la clase (registro) el nombre y sueldo 
        per = Registro(nombre, sueldo)
        
        # Se hara un guardado en la lista vacia (append) 
        # segun los datos de la variable (per)
        lista.append(per)

        # Se da la opcion de guardar o no un empleado mas
        eleccion = input("Desea ingresar otro empleado? (S) o (N): ")
        
        # Capitalizamosel eleccion para poner ahorrar compuertas
        eleccion = eleccion.capitalize()

"""
Cuando el buble detecte que no ingresara mas empleados se enseñara por
pantalla el reporte de cada empleado mas el acumulo de empleados y sueldos
"""
while eleccion == 'N':
    
    # Con solo saltos de linea y tabulaciones se da formato a la tabla
    print("\t\t\tREPORTE EMPLEADOS\n  \
            NOMBRE\t\t\tSUELDO\n  \
            __________________________________")
    
    # Hacemos el llamado a la clase (todos) para que en el print se 
    # acomode cada elemento que teniamos en la lista
    Todos()
    print(f"\t\t{empleados} EMPLEADOS\t\t${salarios:,.0f}")
    print("Programa finalizado")
    break