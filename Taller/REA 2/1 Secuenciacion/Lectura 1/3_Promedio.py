# Promedio estudiante 
"""
Elaborar un algoritmo para calcular el promedio de calificaciones 
de un estudiante. Los datos disponibles para lectura son el nombre, 
el código, calificación1, calificación2, calificación3, y calificación4; 
de cada uno de los cuatro exámenes presentados. La información 
que se debe imprimir es el nombre del estudiante y el promedio 
de calificaciones. 
"""

# Se piden el tipo de estudiantes de tipo texto (string) por teclado
estudiante = input('Ingrese el nombre del estudiante: ')

# Capitalizamos la entrada de estudiante para poner la prier letra en mayus
estudiante = estudiante.capitalize()

# Se piden el codigo de tipo entero (int) por teclado
codigo = int(input('Ingrese el codigo: '))

# Se piden las notas de tipo deciaml (float) por teclado
nota_1 = float(input('Primer calificacion: '))
nota_2 = float(input('Segunda calificacion:  '))
nota_3 = float(input('Tercera calificacion: '))
nota_4 = float(input('Cuarta calificacion:  '))

# Se guarda en la variable (promedio) el resultado de la operacion
promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4

""" 
El mensaje por pantalla tendra un formato (fstring) para
limitar los decimales a uno (1)
"""
print(f"El estudiante {estudiante} tuvo un promedio de: {promedio:.1f}")