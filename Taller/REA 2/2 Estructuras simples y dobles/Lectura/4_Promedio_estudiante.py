# Calcula promedio estudiante con comentario
"""
Elabora un algoritmo para calcular el promedio de calificaciones de 
un estudiante, los datos disponibles para lectura son el nombre,
calificacion 1, calificacion 2, calificacion 3 y calificacion 4; 
de cada uno de los cuatro examenes presentados. La informacion que 
se debe imprimir es el nombre del estudiante, el promedio de 
calificaciones y un comentario de "Aprobado" si obtiene 3.0 o mas, o 
"Reprobado" en caso contrario
"""

# Se pide el nombre de estudiante de tipo texto (string) por teclado
estudiante = input('Ingrese el nombre del estudiante: ')

# Capitalizamos la entrada de empleado para poner la prier letra en mayus
estudiante = estudiante.capitalize()
print('Ingrese las 4 calificaciones')

# Se piden las calificaciones de tipo decimal (float) por teclado
cal_1 = float(input('Calificacion 1: '))
cal_2 = float(input('Calificacion 2: '))
cal_3 = float(input('Calificacion 3: '))
cal_4 = float(input('Calificacion 4: '))

# Se guarda en la variable (promedio) el resultado de la operacion
promedio = (cal_1+cal_2+cal_3+cal_4)/4

"""
Con el bucle if se analiza que el promedio cumpla los
parametros para aprovar, si no entonces reprueba
"""
if promedio >= 3.0:
    comenraio = "APROVADO"
else:
    comenraio = "REPROBADO"


""" 
El mensaje por pantalla tendra un formato (fstring) para 
limitar los decimales a uno (1)
"""
print(f"El estudiante {estudiante} fue {comenraio} con {promedio:.1f}")