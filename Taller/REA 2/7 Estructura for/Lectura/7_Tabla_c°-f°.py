# Tabla conversion grados fagrenheit a celsius
"""
Una temperatura en grados Fahrenheit se convierte a grados Celsius, 
con la siguiente ecuación C=5/9*(F -32). Elaborar un algoritmo que 
imprima una tabla desde 1 hasta 65 ( con intervalos de 1) 
grados Fahrenheit con sus equivalencias en grados Celsius.

        Fahrenheit       Celsius
        ________________________
            1             99.99
            2             99.99
            3             99.99
            .
            .
            .
            65            99.99
"""

# Creamos una funcion para dar formato a la tabla 
def Tabla():
    print("\t\tFahrenheit\tCelsius")
    print("\t","-" * 32)
    
    """
    El bucle for tendra un recorrido de 0 a 65 y se interara en la
    variable (c) dando la formula 1 a 1 de la convercion y dentro de si 
    mismo dara por pantalla el mensaje las 65 conversiones 
    """
    for f in range (0,66,1):
        
        # Formula para pasar a c°
        c = (f-32)*5/9
        
        """
        Con fstring se acomoda el mensaje a la tabla y 
        se da solo dos (2) decimales
        """
        print(f"\t\t{f}°\t\t{c:.2f}°")

Tabla()