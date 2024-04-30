# Determina facultades menores 
"""
Elaborar un algoritmo tal que dado como datos el código de un 
estudiante, la carrera en la que está inscrito, su semestre y 
su promedio; determine si el estudiante es apto para pertenecer 
a alguna de las facultades menores que tiene la universidad. 
Si el estudiante es aceptado teniendo en cuenta las especificaciones 
que se listan a continuación, se debe imprimir su código, carrera y la palabra
“ACEPTADO”.

Especificaciones para pertenecer a las facultades menores:

Economía:       semestre >= 6 , promedio >=8.8
Computación:    semestre > 6 ,  promedio >=9.0
Administración: semestre > 5 ,  promedio >=8.5
Contabilidad:   semestre > 5 ,  promedio >=8.5
"""
print('     ***___ FACULTADES MENORES___***\n')
print('    Economia        Computacion \n\
    Administracion   Contabiilidad\n')

# Se piden el codigo de tipo entero (int) por teclado
codigo = int(input('Ingrese el codigo de estudiiante: '))

# Se pide la carrera de tipo texto (string) por teclado
carrera = input('Ingrese Carrera: ')

# Capitalizamos la entrada de carrera para poner la prier letra en mayus
carrera = carrera.capitalize()

# Se piden la ubicacion de semestre de tipo entero (int) por teclado
semestre = int(input('Ingrese semestre: '))

# Se piden el promedio de tipo decimal (float) por teclado
promedio = float(input('Ingrese el promedio: '))

"""
Se hara un menu con el bucle while y anidado tendra el if que evaluara
el semestre y promedio para dar consigo respuesta a la aprovacion o rechazo
"""
while carrera == "Economia":
    if semestre >= 6 and promedio >= 8.8:
        
        # Se usa un fstring para dar formato a el mensaje
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print('NO ACEPTADO')
        break
while carrera == "Computacion":
    if semestre > 6 and promedio >= 9.0:
        
        # Se usa un fstring para dar formato a el mensaje
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print('NO ACEPTADO')
        break
while carrera == "Administracion":
    if semestre > 5 and promedio >= 8.5:
        
        # Se usa un fstring para dar formato a el mensaje
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print('NO ACEPTADO')
        break
while carrera == "Contabilidad":
    if semestre > 5 and promedio >= 8.5:
        
        # Se usa un fstring para dar formato a el mensaje
        print(f"Estudiante {codigo} de:{carrera} fue ACEPTADO")
        break
    else:
        print('NO ACEPTADO')
        break