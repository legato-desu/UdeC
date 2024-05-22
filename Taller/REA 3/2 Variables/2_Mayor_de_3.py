# Calcula mayor tres numeros enteros
"""
Elaborar un algoritmo que permita leer tres números de tipo entero e 
imprima el mayor, utilizando un método para leer los números, otro 
método para obtener y devolver el mayor y método para imprimir el mayor. 
"""

# Metodo para almacenar los numeros por teclado
def numeros():
    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingresa el segundo numero: "))
    n3 = int(input("Ingresa el tercer numero: "))
    return n1, n2, n3

# En la estructura de este metodo se guardara la comparativa 
# para determinar que numero es el mayor
def mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
    
# Este metodo da por pantalla el numero mayor de los tres ingresados
def salida(final):
    print(f"El mayor es: {final}")

# Se hace el llamado a cada uno de los metodos para ejecutar el codigo
n1, n2, n3 = numeros()
final = mayor(n1,n2,n3)
salida(final)