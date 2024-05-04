# Reporte clientes
"""
Una empresa vende hojas de hielo seco, con las condiciones siguientes:

        Tipo cliente            Descuento
            1                       5%
            2                       8%
            3                       12%
            4                       15%
            
Cuando un cliente realiza una compra se generan los siguientes datos: 
nombre del cliente, tipo de cliente, cantidad de hojas compradas, precio hoja.
Elaborar un algoritmo que permita procesar varios clientes e imprima el 
siguiente reporte:

                            Reporte clientes
        Nombre                  Subtotal        Descuento       Neto pagar
        __________________________________________________________________
        xxxxxx                  99.99            99.99          999.99
        xxxxxx                  99.99            99.99          999.99
        .
        .
        .
        xxxxxx                  99.99            99.99          999.99
        
        Total 999 Clientes      999.99           999.99         9999.99   
"""
# Se crea una clase Reporte para almacenar las variables en la lista
class Reporte:
    def __init__(self,nombre,subtotal,descuento,neto):
        self.nombre = nombre
        self.subtotal = subtotal
        self.descuento = descuento
        self.neto = neto
        
# Se inician variables en limpio para iniciara bucle y alacenar acumuladores
clientes, restos, todo, descuento, total = 0,0,0,0,0

# Eleccion iniciara estatica para dar arranque al bucle while
eleccion = 'S'

# En la lista vacia se almacenaran los datos para al final imprimir en orden
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
        print(f"\t\t{lista[L].nombre}\t\t${lista[L].subtotal:,.0f}\t\t${lista[L].descuento:,.0f}\t\t${lista[L].neto:,.0f}")
        
        # L tendra un aumento de 1 por cada ingreso al bucle hasta que la lista quede en cero
        L += 1
        
"""
El bucle while procesara todo los datos para almacenar en la lista y tambien 
para analizar las formulas 
"""
while eleccion == 'S':
    
        # Se pide el nombre de tipo texto (string) por teclado
        nombre = input("Ingrese el nombre del cliente: ")
        
        # Capitalizamos el nombre para poner la prier letra en mayus
        nombre = nombre.capitalize()
        
        # se pide el tipo de cliente horas y hoja de tipo entero (int)
        tipo_cliente = int(input("Ingrese el tipo de cliente: "))
        
        # se pide el tipo de hojas y hoja de tipo entero (int)
        hojas = int(input("Cuantas hojas compro?: "))
        hoja = int(input("Ingrese el precio por cada hoja: "))
        
        # La variable subtotal tendra un redondeo de decimales y el calculo
        subtotal = round(hojas * hoja)
        
        """
        El ciclo if evauara que el tipo de cliente si este en los parametros
        de no estar, terminara la ejecucion del codigo
        """
        
        if tipo_cliente == 1:
            descuento = subtotal * 0.05   
        elif tipo_cliente == 2:
            descuento = subtotal * 0.08
        elif tipo_cliente == 3:
            descuento = subtotal * 0.12
        elif tipo_cliente == 4:
            descuento = subtotal * 0.15
        else:
            print("Tipo de cliente no valido")
            break
        
        # Neto almacenara el caluclo del descuento 
        neto = subtotal - descuento
        
        # Con fstring se dara un formato en pantalla con puntos centena y sin decimales
        print(f"{nombre} Subtotal: ${subtotal:,.0f} - ${descuento:,.0f} = ${neto:,.0f}")
        
        # Se da la eleccion de guardar o no un empleado mas
        eleccion = input("Desea ingresar otro Cliente? (S/N): ")    
        
        # Capitalizamosel eleccion para poner ahorrar compuertas
        eleccion = eleccion.capitalize()
        
        """
        En las siguientes variables tendremos el registro para pasar a la lista
        vacia donde podremos tener todo sin alterar el valor anterior 
        """
        clientes = clientes + 1
        total = total + subtotal
        restos = restos + descuento
        todo = todo + neto
        
        # Guardaremos en la vairable (per) el registro con la clase Reporte 
        per = Reporte(nombre,subtotal,descuento,neto)
        
        """
        Se hara un guardado en la lista vacia (append) 
        segun los datos de la variable (per)
        """
        lista.append(per)

"""
Cuando el ciclo detecte que no ingresara mas empleados se enseñara por
pantalla el reporte de cada empleado mas el acumulo de empleados y sueldos
"""
while eleccion == 'N':
    
    # Con saltos de linea y tabulaciones se da formato a la tabla
    
    print("\n\t\t\t\t\t\tREPORTE CLIENTES")
    print("\n\t\tNombres\t\tSubtotal\t\tDescuento\t\tNeto pagar")
    print("\t\t","-"*80)
    
    """
    Hacemos el llamado a la clase (todos) para que en el print se 
    acomode cada elemento que teniamos en la lista
    """
    Todos()
    print(f"\n\t\t{clientes} Clientes\t${total:,.0f}\t\t${restos:,.0f}\t\t${todo:,.0f}")
    print("\nPrograma finalizado\n")
    break