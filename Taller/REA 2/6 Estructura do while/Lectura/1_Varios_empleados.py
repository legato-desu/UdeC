# Calcula sueldo varios empleados
"""
Elaborar un algoritmo que calcule e imprima el sueldo de varios 
empleados, cada empleado se tratará en forma similar al problema de 
cálculo de sueldo de un empleado.
"""
# Eleccion tendra como valor inicial (S) para correr el bucle
eleccion = 'S'

# EL bucle while dara toda la secuencia de acciones 
while eleccion == 'S':
        
        # Se pide el nombre de tipo texto (string) por teclado
        nombre = input("Ingrese el nombre del empleado: ")
        
        # Capitalizamosel nombre para poner la prier letra en mayus
        nombre =nombre.capitalize()
        
        # Se piden las horas de tipo entero (int) por teclado
        horas = int(input("Horas trabajadas: "))
        
        # Se piden el valor de hora de tipo decimal (float) por teclado
        valor_h = float(input("Valor de horas trabajadas: "))

        # En la variabe sueldo guardaremos la operacion con redondeo de decimales
        sueldo = round(horas * valor_h)
        
        # Con fstring damos formato con puntuacion centena y cero (0 )decimales
        print(f"{nombre} Sueldo: ${sueldo:,.0f}")

        # Eleccion pedida al usuario si desea ingresar un empleado nuevo o no
        eleccion = input("Desea ingresar otro empleado? (S) o (N): ")
        
        # Capitalizamosel eleccion para poner ahorrar compuertas
        eleccion = eleccion.capitalize()

# Cuando eleccion sea (N) se finaliza el codigo
while eleccion == 'N':
        print("Programa finalizado")
        break