# Calcula sueldo doble
"""
Siguiendo con el ejemplo de calculo de sueldo de un empleado, 
ahora si el numero de horas trabajadas es mayor que 40 se 
paga al doble del valor por hora. En caso de no ser mayor que 40, 
se paga el valor de hora normal
"""

# Se pide el nombre de empleado de tipo texto (string) por teclado
empleado = input('Ingrese el nombre del empleado: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
empleado = empleado.capitalize()

# Se piden las horas de tipo entero (int) por teclado
horas = int(input('Numero de horas trabajadas: '))

# Se piden el trabajo de tipo decimal (float) por teclado
trabajo = float(input('Valor de hora trabajada: '))

"""
Con el bucle if especificamos que horas sea menor o igual a 40
de ser asi se hace el calculo normal de el sueldo, pero 
si es mayor a 40 las horas entonces se paga el doble
"""

if horas <= 40:
    # Se guarda en la variable (sueldo) el resultado de la operacion
    sueldo = horas * trabajo
else:
    # Se guarda en la variable (sueldo) el resultado de la operacion
    sueldo = 40 * trabajo + (horas-40)*trabajo*2

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"Empleado {empleado} sueldo: ${sueldo:,.0f}")