# Calcular mayor de 5 numeros enteros diferentes
"""
Elabora un algoricmo que lea cinco numeros enteros y calcule e 
imprima el mayor. Se supone que son numeros diferentes
"""

print('Ingrese 5 numeros diferentes ')

# Se piden los numeros de tipo entero (int) por teclado
a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))
d = int(input('Numero 4: '))
e = int(input('Numero 5: '))

"""
Este bucle if evalua primero que los numeros no se repitan 
y de ser asi se ingresa a un if anidado para analizar uno a uno
cual es el mayor de ellos
"""
if a!=b and b!=c and c!=d and d!=e:
    if a>b and a>c and a>d and a>e:
        print(f"El numero {a} es mayor")
    elif b>a and b>c and b>d and b>e:
        print(f"El numero {b} es mayor")    
    elif c>a and c>b and c>d and c>e:
        print(f"El numero {c} es mayor")
    elif d>a and d>b and d>c and d>e:
        print(f"El numero {d} es mayor")
    elif e>a and e>b and e>c and e>d:
        print(f"El numero {e} es mayor")

    """
De no cumplir con ninguna de las anteriores condiciones 
el cierre señala que no cumplio con lo pedido
"""
else:
    print('Los numeros deben ser diferentes')