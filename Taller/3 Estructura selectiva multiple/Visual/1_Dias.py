# Dia de la semana
"""
Crea un programa que por medio de una lista de numeros determinada 
pida uno de esos numeros al usuario y segun el numero le diga que dia
hace referencia a ese numero 
"""

# Se pide dia de tipo entero (int) por teclado
dia = int(input('Ingresa un numero del 1 al 7: '))

"""
Con el bucle if miramos si el numero ingresada por teclado esta segun las 
codiciones dadas, de ser asi se retornara un dia segun su valor, si el ingreso
no forma parte de los requisitos se termina la ejecucion 
"""

# Se da formato al mensaje por pantalla con fstring
if dia == 1:
    print(f"El dia {dia} es Domingo")
elif dia == 2:
    print(f"El dia {dia} es Lunes")
elif dia == 3:
    print(f"El dia {dia} es Martes")
elif dia == 4:
    print(f"El dia {dia} es Miercoles")
elif dia == 5:
    print(f"El dia {dia} es Jueves")
elif dia == 6:
    print(f"El dia {dia} es Viernes")
elif dia == 7:
    print(f"El dia {dia} es Sabado")
else:
    print('No ingresaste un numero de 1 a 7')