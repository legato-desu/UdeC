# Reporte lluvias
"""
La comisión nacional del agua, lleva un registro de las lluvias que se 
presentan en todas las poblaciones del estado, de manera que se tienen 
los siguientes datos:  

Población1 : XXXXXXXXXXX 
Lluvia: 99.99 
Lluvia: 99.99 
. 
. 
. 
Lluvia: 99.99             

totLluvia 999.99  

Población2 : XXXXXXXXXXX 
Lluvia: 99.99 
Lluvia: 99.99 
. 
. 
. 
Lluvia: 99.99  
. 
. 
.

Por cada población aparece el dato de lluvia tantas veces haya llovido, 
este dato está en milímetros cúbicos, pudiera darse el caso de que en 
alguna población no traiga ningún dato de lluvia, esto quiere decir 
que no llovió.  

Elaborar un algoritmo que lea estos datos e imprima el siguiente reporte: 

            REPORTE DE LLUVIAS
    POBLACION               TOTAL LLUVIA
    ------------------------------------
    xxxxxxxxxxx                 999.99
    xxxxxxxxxxx                 999.99
    .
    .
    .
    xxxxxxxxxxx                 999.99
    
    total 999 poblaciones       99999.99
    
    total poblaciones No llovio    999
    
Nota: hay la posibilidad que el estado no reporte poblacion
"""

# Se crea una clase Reporte para procesar el nombre y lluvia de lista
class Reporte:
    def __init__(self,nompobla,lluvia):
        self.nompobla = nompobla
        self.lluvia = lluvia

# Se crea una variable para iniciar el bucle while
hay = 'S'

# En la lista vacia se almacenaran con el append los acumuladores
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
        print(f"\t\t{lista[L].nompobla}\t\t\t\t{lista[L].lluvia:.0f}")
        
        # L tendra un aumento de 1 por cada ingreso al bucle hasta que la lista quede en cero
        L += 1

# Se inician variables para almacenar acumuladores en el bucle
totpoblaciones, tottotlluvias, totnollovio = 0, 0, 0

# Se pide la poblacion de tipo texto (string) por teclado
hay = input("Hay poblacion? (S/N): ")

# Capitalizamos la opcion para poner la letra en mayus
hay = hay.capitalize()

"""
El bucle while procesara todo los datos para almacenar en la lista y tambien 
para analizar las formulas 
"""
while hay == 'S':
    
        # Se pide el nombre de tipo texto (string) por teclado
        nompobla = input("Ingrese el nombre de la poblacion: ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        nompobla = nompobla.capitalize()
        
        # Se inicializa la variable para guardar total lluvias
        totlluvia = 0
        
        # Se pregunta si hay mas lluvias 
        otra = input("Hay otra lluvia? (S/N): ")
        
        # Capitalizamos la opcion para poner la letra en mayus
        otra = otra.capitalize()
        
        """
        El bucle while anidado procesara todo los datos para almacenar en la 
        lista y tambien para analizar las formulas 
        """
        while otra == 'S':
            
            # Se pide la cantidad de lluvia tipo decimal (float) por teclado
            lluvia = float(input("Cantidad de lluvia (milimetro cubicos): "))
            
            # Se hace un incremento en la totalidad de lluvias
            totlluvia += lluvia
            
            # Se pregunta si hay mas lluvias 
            otra = input("Hay otra lluvia? (S/N): ")
        
        # Con fstring se da formato al mensaje en pantalla
        print(f"Poblacion: {nompobla}, LLuvia: {totlluvia:.0f}")
        
        # Estas variables haran un incremento por cada recorrido
        totpoblaciones += 1
        tottotlluvias += totlluvia
        
        # Si no hay lluvias entonces se agrega a la opcion de no llovio
        if totlluvia == 0:
            totnollovio += 1
        
        # Se pregunta si hay mas poblacion 
        hay = input("Hay poblacion? (S/N): ")

        # Capitalizamos la opcion para poner la letra en mayus
        hay = hay.capitalize()
        
        # Se usa fstring para dar formato al mensaje en pantalla
        print(f"Poblacion: {totpoblaciones}, Lluvias: {tottotlluvias}, Sin lluvia: {totnollovio}")
        
        # Guardaremos en la clase (Reporte) la poblacion y lluvia 
        reporte = Reporte(nompobla, lluvia)
        
        """
        Se hara un guardado en la lista vacia (append) 
        segun los datos de la variable (reporte)
        """
        lista.append(reporte)
        
"""
Cuando el buble detecte que no ingresara mas empleados se enseñara por
pantalla el reporte de cada empleado mas el acumulo de empleados y sueldos
"""
while hay == 'N':
    
    # Con solo saltos de linea y tabulaciones se da formato a la tabla
    print("\n\t\t\t\tREPORTE DE LLUVIAS\n\t\tPOBLACION\t\t\tTOTAL LLUVIA")
    print("\t\t","-" * 40)
    
    """    
    Hacemos el llamado a la clase (todos) para que en el print se 
    acomode cada elemento que teniamos en la lista
    """
    
    Todos()
    print(f"\n\t\tTotal {totpoblaciones} Poblaciones\t\t\t{tottotlluvias:.0f}")
    print(f"\n\t\tTotal poblaciones no llovio\t\t{totnollovio}")
    print("\nPrograma finalizado\n")
    break