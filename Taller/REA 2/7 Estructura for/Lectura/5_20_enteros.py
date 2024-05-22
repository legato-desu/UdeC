# Calcula la suma de 20 numeros enteros

"""
Elaborar un algoritmo que lea 20 números enteros y que calcule e 
imprima el promedio de dichos números.
"""

# Se inicia la constante en cero
suma = 0


# En el bucle for se pedira 20 veces por pantalla un numero
for i in range (20):
    
    # Se pide un numero de tipo entero (int) por teclado
    num = int(input("Ingrese numero: "))
    
    # La variable suma tendra el cumulo de sumar los 20 numeros por teclado
    suma = suma + num

# Al salir del bucle se tomara la suma total y se dividira segun el promedio 
promedio = suma / 20

# Con fstring se dara el resultado final de el promedio tras la suma

print(f"Total {suma}, promedio {promedio}")