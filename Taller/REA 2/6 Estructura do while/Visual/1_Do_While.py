# Con Do While

"""
Con el bucle if se pedira al humano una letra especifica con un mensaje
de error en caso que no lo acate
"""

while True:
    
    # Se pide la letra de tipo texto (string) por teclado
    letra = input("Humano digita la tecla 'a': ")
    
    # Si la letra no es 'a' se dara el mensaje por pantalla predefinido
    if letra != 'a':
        break
print("Humano tonto te dije que precionnaras la tecla 'a' ")

"""
# Con While 
letra = input("Humano digita la tecla 'a': ")
while letra == 'a':
    letra = input("Humano digita la tecla 'a': ")
print("Humano tonto te dije que precionaras la teccla 'a'")
"""