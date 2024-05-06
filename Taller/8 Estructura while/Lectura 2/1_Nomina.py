# Nomina quincenal
"""
El sueldo que perciben los vendedores de una empresa automotriz, 
está integrado de la siguiente manera. El salario mínimo (quincenal), 
más $100000 por cada auto vendido, más el 2% del valor de los autos vendidos. 

Sueldo = SalarioMinimo + 100000*TotalAutosVendidos+ TotalVendido*0.02  

Datos que se tienen por cada vendedor: 
Nombre del vendedor: XXXXXXXXXXXXXXXX  
precioAuto: 999999.99       
precioAuto: 999999.99       
.       
.       
precioAuto: 999999.99 
Nombre del vendedor: XXXXXXXXXXXXXXXX       
precioAuto: 999999.99       
precioAuto: 999999.99       
.       
.       
precioAuto: 999999.99 
. 
. 
.  

Como se puede apreciar, se tienen varios vendedores; por cada vendedor se 
tiene el nombre y el precio de cada auto vendido en la quincena. 
Es posible que algunos vendedores  no hayan realizado venta alguna, 
en tal caso solo se le paga el salario mínimo quincenal. 
Elaborar un algoritmo que permita leer los datos  e 
imprimir el siguiente reporte: 

                NOMINA QUINCENAL
        NOMBRE VENDEDOR             SUELDO
        ------------------------------------
        XXXXXXXXXXXXXX              99999.99
        XXXXXXXXXXXXXX              99999.99
        .
        .
        .
        XXXXXXXXXXXXXX              99999.99
        
        TOTAL 999 VENDERORES       9999999.99

"""

# Se crea una clase Nomina para procesar el nombre y sueldo de lista
class Nomina:
    def __init__(self,nomvend,sueldo):
        self.nomvend = nomvend
        self.sueldo = sueldo

# Se crea una variable para iniciar el bucle while
eleccion = 'S'

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
        print(f"\t\t{lista[L].nomvend}\t\t\t\t${lista[L].sueldo:,.0f}")
        
        # L tendra un aumento de 1 por cada ingreso al bucle hasta que la lista quede en cero
        L += 1

# Se pide el salario minimo de tipo entero (int) por teclado
sal_min = int(input("Ingrese el salario minimo quincenal: "))

# Se inician variables para almacenar acumuladores en el bucle
totvendedores, totsueldos = 0, 0

"""
El bucle while procesara todo los datos para almacenar en la lista y tambien 
para analizar las formulas 
"""
while eleccion == 'S':
    
        # Se pide el nombre de tipo texto (string) por teclado
        nomvend = input("Ingrese el nombre del vendedor: ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        nomvend = nomvend.capitalize()
        
        # Se inician variables para almacenar acumuladores en el bucle
        totautos, totvendido = 0, 0
        
        # Se pide la otra opcion de tipo texto (string) por teclado
        otro = input("Hay otro auto vendido? (S/N): ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        otro = otro.capitalize()
        
        """
        El bucle while anidado procesara todo los datos para almacenar en la 
        lista y tambien para analizar las formulas 
        """
        while otro == 'S':
            
            # Se pide el salario minimo de tipo entero (int) por teclado
            precio_auto = int(input("Ingrese el precio del auto: "))
            
            # Se guarda un acumulador en la variable totautos
            totautos += 1
            
            # Se guarda un acumulador en la variable totvendido
            totvendido += precio_auto
            
            # Se pide la otra opcion de tipo texto (string) por teclado
            otro = input("Hay otro auto vendido? (S/N): ")
        
            # Capitalizamos el nombre para poner la prier letra en mayus
            otro = otro.capitalize()
            
        # Sueldo almacenara el calculo de la formula   
        sueldo = sal_min + 100000 * totautos + totvendido * 0.02
        
        # Con fstring se da formato al pre-texto por pantalla 
        print(f"{nomvend}, sueldo: ${sueldo:,.0f}")
        
        # Se guarda un acumulador en la variable totvendedores
        totvendedores += 1
        
        # Se guarda un acumulador en la variable totsueldos
        totsueldos += sueldo
        
        # Guardaremos en la clase (Nomina) el nombre y sueldo 
        vendedores = Nomina(nomvend, sueldo)
        
        """
        Se hara un guardado en la lista vacia (append) 
        segun los datos de la variable (vendedores)
        """
        lista.append(vendedores)
        
        # Se pide el nombre de tipo texto (string) por teclado
        eleccion = input("Desea procesar otro vendedor? (S/N): ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        eleccion = eleccion.capitalize()
        
"""
Cuando el buble detecte que no ingresara mas empleados se enseñara por
pantalla el reporte de cada empleado mas el acumulo de empleados y sueldos
"""
while eleccion == 'N':
    
    # Con solo saltos de linea y tabulaciones se da formato a la tabla
    print("\t\t\t\tNOMINA QUINCENAL\n\t\tNOMBRE VENDEDOR\t\t\tSUELDO")
    print("\t\t","-" * 37)
    
    """    
    Hacemos el llamado a la clase (todos) para que en el print se 
    acomode cada elemento que teniamos en la lista
    """
    
    Todos()
    print(f"\n\t\t{totvendedores} EMPLEADOS\t\t\t${totsueldos:,.0f}")
    print("\nPrograma finalizado\n")
    break