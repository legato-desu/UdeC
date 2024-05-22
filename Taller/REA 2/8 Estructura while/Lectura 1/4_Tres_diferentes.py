# Imprime numeros del 1 al 10
"""
Elaborar un algoritmo que imprima los números enteros del 1 al 10, de 
tres formar diferentes 
a. Utilizando FOR 
b. Utilizando Do while 
c. Utilizando While 
"""

print('Menu de opcopnes:\n  \
        a = Utilizando FOR\n  \
        b = Utilizando Do while \n  \
        c = Utilizando While')

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
    
    # El bucle while es la opcion del usuario y dentro esta la funcion
    while opcion == 'A':
        print('OPCION A')
        # Utilizando FOR 
        
        # Enseñara por pantalla el valor de u en cada vuelta hasta completar el rango
        for i in range (1,11):
            print(i)
        break
    
    # El bucle while es la opcion del usuario y dentro esta la funcion
    while opcion == 'B':
        print('OPCION B')
        # Utilizando Do while
        
        print(f"\tPython no tiene una funcionalidad específica para crear un bucle do while\n\
            cómo otros lenguajes. Pero es posible emular un bucle do while en Python\n")
        
        # Esta es una simulacion de un bucle do while en python
        
        # Asignamos a una variable el valor de 1
        vuelta = 1
        
        # Como while ya es verdadero se ejecutara directamente el codigo
        while True:

            # Se da por pantalla el valor de cada ejecucion del bucle
            print(vuelta)
            
            # Se incrementa en 1 por cada vuelta dada
            vuelta += 1
            
            # Una vez que la vuelta sea mayor de 10 se rompe el bucle 
            if vuelta > 10:
                break
        break
    
    # El bucle while es la opcion del usuario y dentro esta la funcion
    while opcion == 'C':
        print('OPCION C')
        # Utilizando While
        
        # Asignamos a una variable el valor de 1
        vuelta = 1
        
        # Se hara un ciclo siempre y cuando la vuelta o supere la condicion
        while vuelta <= 10:
            
            # Mensaje por pantalla de el valor de cada vuelta
            print(vuelta)
            
            # Se hace un incremento para cumplor con la condicion del bucle
            vuelta += 1
        
        break
else:
    print('Opcion no valida')