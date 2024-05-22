# Calcula cambio cliente
"""
Elaborar un algoritmo talque dado el precio de un artículo 
vendido y la cantidad de dinero entregada por el cliente, 
que calcule e imprima el cambio que se le debe entregar al mismo
"""

# Se piden el articulo y cantidad de tipo deciaml (float) por teclado
articulo = float(input('Ingrese el precio del articulo: '))
cantidad = float(input('Ingrese la cantidad pagada: '))

# Se guarda en la variable (cambio) el resultado de la operacion
cambio = cantidad - articulo

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puncuacion 
de centenas y limitar los decimales a cero (0)
"""
print(f"El cambio es de: ${cambio:,.0f}")