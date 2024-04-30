# Calcular mayor de tres numeros
"""
Elaborar un algoritmo que lea tres números enteros diferentes,  
que calcule e imprima el mayor. Hacerlo de tres formas diferente, 
así: 
a. Utilizando   If then / else 
b. Utlizando    if then  y  AND 
c. Utilizando   if then/ else y AND 
"""

print('Menu de opcopnes:\n  \
        a = If then / else\n  \
        b = if then  y  AND \n  \
        c = if then/ else y AND')

# Se pide la opcion de tipo texto (string) por teclado
opcion = input('Ingrese su opcion elegida: ')

# Capitalizamos la opcion para poner la letra en mayus
opcion = opcion.capitalize()

"""
Por medio del buble if se mira si el ingreso por teclado es parte
de la lista ya definida y asi dar el mensaje por pantalla segun
corresponda
"""
if opcion == 'A' or  opcion == 'B' or opcion == 'C':
    
    # Utilizando  If then / else 
    while opcion == 'A':
        print('OPCION A')
        
        # Se piden los numeros de tipo entero (int) por teclado
        num_1 = int(input('Ingrese el primer numero: '))
        num_2 = int(input('Ingrese el segundo numero: '))
        num_3 = int(input('Ingrese el tercer numero: '))
        
        # El bucle if de forma anidada evaluara cual de ellos es mayor
        if num_1 > num_2:
            if num_1 > num_3:
                
                # Se da formato fstring para el mensaje en pantalla
                print(f"El numero mayor es {num_1}")
            else:
                # Se da formato fstring para el mensaje en pantalla
                print(f"El numero mayor es {num_3}")
        
        # El bucle if de forma anidada evaluara cual de ellos es mayor
        elif num_2 > num_3:
            
            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_2}")
        else:
            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_3}")
        break

    # Utlizando  if then  y  AND 
    while opcion == 'B':
        print('OPCION B')
        
        # Se piden los numeros de tipo entero (int) por teclado
        num_1 = int(input('Ingrese el primer numero: '))
        num_2 = int(input('Ingrese el segundo numero: '))
        num_3 = int(input('Ingrese el tercer numero: '))

        """
        El bucle if de forma anidada evaluara por medio de compuertas para 
        ver cual de ellos es mayor
        """
        if (num_1 > num_2) and (num_1 > num_3):

            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_1}")
        elif num_2 > num_1 and num_2 > num_3:

            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_2}")
        elif num_3 > num_1 and num_3 > num_2:

            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_3}")
        break

    # Utilizando  if then/ else y AND
    while opcion == 'C':
        print('OPCION C')
        
        # Se piden los numeros de tipo entero (int) por teclado
        num_1 = int(input('Ingrese el primer numero: '))
        num_2 = int(input('Ingrese el segundo numero: '))
        num_3 = int(input('Ingrese el tercer numero: '))
    
        """
        El bucle if de forma simple evaluara por medio de compuertas para 
        ver cual de ellos es mayor
        """
        if (num_1 > num_2) and (num_1 > num_3):
            
            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_1}")
        elif num_2 > num_3:
            
            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_2}")
        else:
            
            # Se da formato fstring para el mensaje en pantalla
            print(f"El numero mayor es {num_3}")
        break
else:
    print('Opcion no valida')