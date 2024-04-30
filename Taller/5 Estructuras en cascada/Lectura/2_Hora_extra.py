# Calcula sueldo con horas extra
"""
Elaborar un algoritmo que permita calcular lo que hay que 
pagarle a un trabajador teniendo en cuenta su sueldo y las horas 
extras trabajadas. Para el pago de horas extras se tiene en 
cuenta la categoría del trabajador, de acuerdo con la siguiente tabla.

Categoria       Precio hora extra
    1               $10.000
    2               $15.000
    3               $20.000
    4               $25.000
    
A los trabajadores con categoría mayor a 4 no se les pagan horas extras. 
Cada trabajador puede tener como máximo 30 horas extra, si tiene más 
se le pagarán 30. El algoritmo debe imprimir nombre del trabajador, 
categoría, nuevo sueldo.
"""

# Se pide el nombre de trabajador de tipo texto (string) por teclado
trabajador = input('Ingrese el nombre del trabajador: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
trabajador = trabajador.capitalize()

# Se piden la categoria de tipo entero (int) por teclado
categoria = int(input('Ingrese categoria: '))

# Se piden el sueldo de tipo decimal (float) por teclado
sueldo = float(input('Ingrese sueldo: '))

# Se piden las horas de tipo entero (int) por teclado
horas = int(input('Ingrese numero de horas extra: '))

"""
El bucle if analizara el la categoria y segun el filtro guardara una
variable (precio) con un monto predefinido 
"""
if categoria == 1:
    precio = 10000
elif categoria == 2:
    precio = 15000
elif categoria == 3:
    precio = 20000
elif categoria == 4:
    precio = 25000
else:
    precio = 0

"""
El bucle if determinara las horas trabajadas siendo que si son mayores de
30 se hara un recargo en el total
"""
if horas <= 30:
    total = sueldo + horas * precio
else:
    total = sueldo + 30 * precio

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"El trabajador {trabajador} categoria {categoria} tendra un total de ${total:,.0f}")