# Calcula mayor de dos numeros diferentes
"""
Elabora un algoritmo que lea dos numeros enteros diferenes 
y que calcule e imprimael mayor
"""

print('Ingrese dos numeros enteros diferentes')

# Se piden los numeros de tipo entero (int) por teclado
num_1 = int(input('Numero 1: '))
num_2 = int(input('Numero 2: '))

"""
Con el bucle if primero analizamos si los numeros son diferentes, de no 
ser asi se termina la ejecucion, una vez pasada la primer condicional 
solo resta analizar cual de los dos numeros es mayor 
"""
if num_1 == num_2:
    print('Los numeros deben ser diferentes')
elif num_1 > num_2:
    print(f"El numero {num_1} es mayor")
else:
    print(f"El numero {num_2} es mayor")