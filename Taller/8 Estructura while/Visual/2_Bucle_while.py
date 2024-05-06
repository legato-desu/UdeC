# Bucle while
"""
Crea un programa que por medio de un bucle while imprima una alerta por
pantalla segun su incremento de dos en dos teninedo de limite el bucle un 100
desde 1
"""

# Iniciamos la constante en 1 para dar inicio al bucle 
site = ""

"""
Mientras el sitio (site) sea diferente a la entrada no finalizara el bucle
"""
while site != "Unicundi":
    
    # Se pide el nombre del sitio de tipo texto (string) por teclado
    site = input("Ingresa tu sitio web preferido: ")
    
    # Capitalizamos la entrada de site para poner la prier letra en mayus
    site = site.capitalize()
