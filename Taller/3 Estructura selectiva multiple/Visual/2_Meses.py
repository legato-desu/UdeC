# Meses
"""
Crea un prograa para determinar que mes es segun la inicial de 
dicho mes introducida por el usuario
"""

print('Digita una de estas letras')

# Se pide una letra de tipo texto (string) por teclado
mes = input('E, F, M, A, J: ')

# Capitalizamos la entrada de mes para ahorrar compuertas en el codigo
mes = mes.capitalize()

"""
Con el bucle if miramos si la letra ingresada por teclado esta segun las 
codiciones dadas, de ser asi se retornara un mes segun su inicial, si el ingreso
no forma parte de los requisitos se termina la ejecucion 
"""

# Se da formato al mensaje por pantalla con fstring

if mes == 'E':
    print(f"El mes ({mes}) es Enero")
elif mes == 'F':
    print(f"El mes ({mes}) es Febrero")
elif mes == 'M':
    print(f"El mes ({mes}) es Marzo")
elif mes == 'A':
    print(f"El mes ({mes}) es Abril")
elif mes == 'J':
    print(f"El mes ({mes}) es Junio")
else:
    print('Ingreso no valido')
