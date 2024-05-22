# Transaccion
"""
Crea un programa que dado los siguientes datos de entrada: 
saldo anterior, tipo de movimiento R (retiro) o D (deposito) 
y monto de transaccion, obtener como dato la salida el saldo actual
"""

print('(D) Deposito\n(R) Retiro')

# Se pide el tipo de movimiento de tipo texto (string) por teclado
tipo_movimiento = input('Tipo de movimiento (D) o (R): ')

# Capitalizamos la entrada de movimiento para ahorrar compuertas en el codigo
tipo_movimiento = tipo_movimiento.capitalize()

# Se piden el saldo anterior de tipo entero (int) por teclado
santerior = int(input('Ingrese el saldo anterior: '))

"""
Con el bucle if determinamos que tipo de accion realizar ya sea D o R
en cada segmneto se hara una opearacion diferente, de no haber ingresado 
una opcion valida el bucle finaliza y termina la ejecucion
"""
if tipo_movimiento == 'D':
    
    # Se piden el monto de tipo entero (int) por teclado
    monto_transaccion = int(input('ingrese el nuevo monto: '))
    
    # Se guarda en la variable (sactual) el resultado de la operacion
    sactual = santerior + monto_transaccion
    
    # Se da formato al mensaje por pantalla con fstring
    print(f"Saldo actual: ${sactual:,.0f}")
    
elif tipo_movimiento == 'R':
    
    # Se piden el monto de tipo entero (int) por teclado
    monto_transaccion = int(input('ingrese el nuevo monto: '))
    
    # Se guarda en la variable (sactual) el resultado de la operacion
    sactual = santerior - monto_transaccion
    
        # Se da formato al mensaje por pantalla con fstring
    print(f"Saldo actual: ${sactual:,}")
    
else:
    print('Movimiento no valido')