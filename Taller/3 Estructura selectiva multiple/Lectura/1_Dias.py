# Dice dia de la semana
"""
Elaborar un algoritmo que lea un número de día (un valor de a 1 a 7) ; e 
imprima domingo si es 1, lunes si es 2, ….., sábado si e 7.  
"""
# Se piden el dia de tipo entero (int) por teclado
dia = int(input('Ingresa un numero del 1 al 7: '))


"""
El bucle if manejara una secuencia de acciones con el fin de analizar
el numero por teclado, de ser parte de las condicionales permitidas
dara un dia por pantalla de no ser asi terminara la ejecucion
"""
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Lunes')
elif dia == 3:
    print('Martes')
elif dia == 4:
    print('Miercoles')
elif dia == 5:
    print('Jueves')
elif dia == 6:
    print('Viernes')
elif dia == 7:
    print('Sabado')
else:
    print('El numero no esta en el rango del 1 a 7')