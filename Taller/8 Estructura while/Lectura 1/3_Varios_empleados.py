# Calcula sueldo de varios empleados
"""
Elaborar un algoritmo que permita procesar varios empleados, 
igual al primer ejemplo de Do while pero con la posibilidad que 
No se procese ningún empleado (o que No se realice el ciclo repetitivo) 
"""

# Se pide la eleccion de tipo texto (string) por teclado
eleccion = input("Deseia procesar otro empleado? (S/N) ")

# Capitalizamos la eleccion para poner la letra en mayus
eleccion = eleccion.capitalize()

# El bucle while es la opcion del usuario y dentro esta la funcion
while eleccion == 'S':
    
    # Se pide el nombre del empleado de tipo texto (string) por teclado
    nombre = input("Ingrese el nombre del empleado: ")
    
    # Capitalizamos la eleccion para poner la letra en mayus
    nombre = nombre.capitalize()
    
    # Se piden las horas y su valor de tipo entero (int)
    horas = int(input("Total de horas trabajadas: "))
    valor = int(input("Valor de cada hora: "))
    
    # En la variable sueldo se ejecuta la operacion
    sueldo = horas * valor
    
    """
    Con fstring damos formato al texto en pantalla y se da puntos centena
    y cero (0) decimales
    """
    print(f"{nombre} sueldo de: ${sueldo:,.0f}")
    
    # Se pide la eleccion de tipo texto (string) por teclado
    eleccion = input("Deseia procesar otro empleado? (S/N) ")
    
    # Capitalizamos la eleccion para poner la letra en mayus
    eleccion = eleccion.capitalize()