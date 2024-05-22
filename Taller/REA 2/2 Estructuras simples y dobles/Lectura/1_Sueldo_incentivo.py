# Calcula sueldo empleado con incentivo
"""
Siguiendo con el mismo ejemplo de calculo de sueldo de un empleado,
ahora se otorga un incentivo de 5% del sueldo, si el empleado 
trabaja mas de 40 horas; es decir, al sueldo se le agrega el 
5% del mismo sueldo
"""

# Se pide el nombre de empleado de tipo texto (string) por teclado
empleado = input('Ingrese el nombre del empleado: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
empleado = empleado.capitalize()

# Se piden las horas de tipo entero (int) por teclado
horas = int(input('Numero de horas trabajadas: '))

# Se piden el valor_hora de tipo decimal (float) por teclado
valor_hora = float(input('Valor de las horas trabajadas: '))

# Se guarda en la variable (sueldo) el resultado de la operacion
sueldo = horas * valor_hora

# Con el bucle if se evalua que horas sea mayor o igual a 40
if horas >= 40:
    
    # Si se cumple la dondicion entonces a sueldo se le da un 5%
    sueldo = sueldo + sueldo*0.05
    
""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"{empleado} tendra un sueldo de: ${sueldo:,.0f}")