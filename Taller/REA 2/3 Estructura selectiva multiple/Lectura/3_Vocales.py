# Dice vocal minuscula o vocal mayuscula 
"""
Elaborar un algoritmo tal que lea una letra e imprima 
la letra, y  si es vocal minúscula o vocal mayúscula. 
"""

# Se crea una lista fija con la vocales ya definidas
vocales = ["a","i","u","e","o"]

# Se pide una vocal de tipo texto (string) por teclado
vocal = input('Ingrese una vocal: ')

"""
Por medio del buble if se mira si el ingreso por teclado es parte
de la lista ya definida y asi dar el mensaje por pantalla segun
corresponda
"""

if vocal not in vocales:
    
    # Se da formato al mensaje por pantalla con fstring
    print(f"'{vocal}' esta en Mayuscula")
    
else:
    
    # Se da formato al mensaje por pantalla con fstring
    print(f"'{vocal}' esta en minuscula")