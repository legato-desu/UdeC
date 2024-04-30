# Busqueda de empleo
"""
Escribir un programa que indique si una persona puede trabajar, 
para ello deberia: Estar desempleado y ser mayor de edad.
(Indica con un mensaje en caso de no cumplir alguno de los requisitos).
"""

# Se pide el nombre del usuario de tipo texto (string) por teclado
usuario = input('Ingrese el nombre del usuario: ')

# Capitalizamos la entrada de usuario para poner la prier letra en mayus
usuario = usuario.capitalize()

# Se pide el requisito de empleo de tipo texto (string) por teclado
empleo = input('Busca trabajo? (Si o No): ')

# Capitalizamos la entrada de empleo para poner la prier letra en mayus
empleo = empleo.capitalize()

"""
Se crea un if anidado para determinar primero si esta buscando empleo o no
luego el siguiente if pide la edad, si es mayor de edad dira que puede trabajar,
si no entonces se dara un aviso de menor de edad
"""

if empleo == "Si":
    
        # Se piden las horas de tipo entero (int) por teclado
        edad = int(input('Ingrese la edad: '))
        
        if edad >= 18:
            
            # Se da formato al mensaje por pantalla con fstring
            print(f"{usuario} puede trabajar")
        else:

            # Se da formato al mensaje por pantalla con fstring
            print(f"{usuario} aun es menor de edad")
else:

    # Se da formato al mensaje por pantalla con fstring
    print(f"{usuario} ya tiene empleo")