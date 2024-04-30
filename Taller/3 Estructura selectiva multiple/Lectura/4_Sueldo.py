# Calcula auento de sueldo segun categoria
"""
Elaborar un algoritmo tal que dado como datos el nombre, 
cédula, la categoría y el sueldo de un trabajador, que calcule el 
aumento correspondiente del sueldo, teniendo en cuenta la siguiente tabla. 

Categoria           Aumento
    1                 15%
    2                 10%
    3                 8%
    4                 7%

E imprima  el nombre, cédula,  y el nuevo sueldo. 
"""

print('Categoria           Aumento\n\
    1                 15%\n\
    2                 10%\n\
    3                 8%\n\
    4                 7%')


# Se pide el nombre de trabajador de tipo texto (string) por teclado
trabajador = input('Ingrese el nombre del trabajador: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
trabajador = trabajador.capitalize()

# Se piden el valor de cedula, categoria y sueldo de tipo entero (int) por teclado
cedula = int(input('Ingresa la cedula: '))
categoria = int(input('Ingrese la categoria: '))
sueldo = float(input('Ingrese el sueldo: '))

"""
Con el bucle while se despliega un analicis para dar consigo el valor segun
la categoria en la que pertenece el empleado y asi dar el aumento correspondiente
"""
while categoria == 1:
    # Se guarda en la variable (nsueldo) el resultado de la operacion
    nsueldo = sueldo + sueldo*0.15
    break
while categoria == 2:
    # Se guarda en la variable (nsueldo) el resultado de la operacion
    nsueldo = sueldo + sueldo*0.10
    break
while categoria == 3:
    # Se guarda en la variable (nsueldo) el resultado de la operacion
    nsueldo = sueldo + sueldo*0.08
    break
while categoria == 4:
    # Se guarda en la variable (nsueldo) el resultado de la operacion
    nsueldo = sueldo + sueldo*0.07
    break

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puntuacion
de centenas y limitar los decimales a cero (0)
"""
print(f"{trabajador} CC:{cedula:,} sueldo: ${nsueldo:,.0f}")