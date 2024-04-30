#  Conversor Ton-Kgr  y  Pies-Mts
"""
Elaborar un algoritmo tal que dado como datos el nombre de un 
dinosaurio, su peso  y su longitud, expresados estos 
dos últimos en toneladas y pies respectivamente; que 
imprima el nombre del dinosaurio, su peso en kilogramos y 
su longitud en metros. 
"""
# Se piden el tipo de dinosaurio de tipo texto (string) por teclado
dinosaurio = input('Ingrese el noombre del dinosaurio: ')
# Capitalizamos la entrada de dinosaurio para poner la prier letra en mayus
dinosaurio = dinosaurio.capitalize()

# Se piden el peso y longitud de tipo entero (int) por teclado
peso = int(input('Ingrese el peso en toneladas: '))
longitud = int(input('Ingrese longitud en pies: '))

# Se guarda en sus respectivas variables el resultado de la operacion
peso_kilo = peso*1000
longitud_pies = longitud*0.32

""" 
El mensaje por pantalla tendra un formato (fstring) para
dar formato al texto y a peso_kilo damos puntos de centena
"""
print(f"El dinosaurio {dinosaurio} pesa {peso_kilo:,} kilos, con una longitud de {longitud_pies} pies" )