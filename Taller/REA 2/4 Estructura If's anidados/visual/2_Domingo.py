# Dias semanales
"""
Escribir un programa que dado un numero indique el dia de la 
semana equivalente iniciando en Domingo = 0
"""

print('Dias de la semana')

# Se piden los numeros de tipo entero (int) por teclado
dias = int(input('Ingrese un numero de 0 a 7: '))

"""
Con el bucle if se hace un analisis y segun el numero ingresado
se registrara la opcion para enseñar por pantalla el dia correspondiente
"""
if dias == 0:
    print('Domingo')
elif dias == 1:
    print('Lunes')
elif dias == 2:
    print('Martes')
elif dias == 3:
    print('Miercoles')
elif dias == 4:
    print('Jueves')
elif dias == 5:
    print('Viernes')
elif dias == 6:
    print('Sabado')
else:
    print('Numero no valido')