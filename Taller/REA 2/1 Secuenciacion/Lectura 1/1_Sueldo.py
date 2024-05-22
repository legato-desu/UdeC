# Calcula sueldo empleado
"""
Elaborar un algoritmo tal que dado como datos el nombre de 
un empleado, el valor de la hora trabajada y  número de horas 
trabajadas, que permita calcular su sueldo e imprima el nombre 
del empleado y su sueldo. 
"""
# Se pide el nombre de empleado de tipo texto (string) por teclado
empleado = input('Ingrese el nombre del empleado: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
empleado = empleado.capitalize()

# Se piden el valor y total de horas de tipo entero (int) por teclado
valor_horas = int(input('Ingrese el valor de la hora trabajada: '))
total_horas = int(input('Ingrese el total de horas trabajadas: '))

# Se guarda en la variable (sueldo) el resultado de la operacion
sueldo = valor_horas * total_horas

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"El empleado {empleado} tendra un sueldo de: ${sueldo:,.0f}")