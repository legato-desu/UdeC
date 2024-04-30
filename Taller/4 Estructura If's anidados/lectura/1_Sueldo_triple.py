# Calculo sueldo triple empleado
"""
Elaborar un algoritmo similar al anterior de 
CALCULO DE SUELDO DOBLE DE UN EMPLEADO, pero ahora teniendo en 
cuenta que se tiene otra alternativa: las horas que exceden de 50 
se pagan al triple del valor por hora. 
"""

# Se pide el nombre del empleado de tipo texto (string) por teclado
empleado = input('Nombre del empleado: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
empleado = empleado.capitalize()

# Se piden el valor_hora y trabajo de tipo decimal (float) por teclado
hora = float(input('Valor de horas trabajadas: '))
trabajo = float(input('Numero de horas trabajadas: '))

"""
El bucle if evalua y segun sus horas de trabajo se dara una bonificacion
"""
if trabajo <= 40:
    # Se guarda en la variable (sueldo) el resultado de la operacion
    sueldo = hora * trabajo
elif trabajo <= 50:
    # Se guarda en la variable (sueldo) el resultado de la operacion
    sueldo = 40 * trabajo + (hora - 40) * trabajo * 2
else:
    # Se guarda en la variable (sueldo) el resultado de la operacion
    sueldo = 40 * trabajo + 10 * trabajo * 2 + (hora - 50 ) * trabajo * 3 
    
""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"{empleado} tendra un sueldo de ${sueldo:,.0f}")