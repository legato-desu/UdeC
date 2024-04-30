# Calcula precio venta articulo
"""
Elaborar un algoritmo que calcule e imprima el precio de venta de 
un artículo. Se tiene los datos  descripción de artículo y el costo de 
producción. El precio de venta se calcula  añadiéndole al costo 120% 
como utilidad y el 15% de impuesto. 
"""
# Se piden el tipo de articulo de tipo texto (string) por teclado
articulo = input('Ingrese la descripcion del articulo: ')

# Capitalizamos la entrada de articulo para poner la prier letra en mayus
articulo = articulo.capitalize()

# Se piden el costo de tipo deciaml (float) por teclado
costo = float(input('Ingrese el costo de produccion: '))

# Se guarda en la variable (venta) el resultado de la operacion
venta = costo + costo * 1.2 + (costo + costo * 1.2) * 0.15

""" 
El mensaje por pantalla tendra un formato (fstring) para poner puncuacion 
de centenas y limitar los decimales a cero (0)
"""
print(f"El articulo {articulo} tiene un precio de venta por: ${venta:,.0f}")