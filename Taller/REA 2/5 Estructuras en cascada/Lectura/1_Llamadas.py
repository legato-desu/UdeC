# Calcular el costo de llamadas internacionales 
"""
Elaborar  un algoritmo que permita calcular  
e imprimir el costo total de una llamada.

CLAVE   ZONA                PRECIO
12      América del Norte   2                   
15      América Central     2.2
18      América del Sur     4.5
19      Europa              3.5
23      Asia                6
25      África              6
29      Oceanía             5
"""
print('     CLAVE           ZONA           PRECIO \n  \
    12      América del Norte       2 \n  \
    15      América Central         2.2 \n  \
    18      América del Sur         4.5 \n  \
    19      Europa                  3.5 \n  \
    23      Asia                    6 \n  \
    25      África                  6 \n  \
    29      Oceanía                 5\n  ')


# Se piden la clave y minutos  de tipo entero (int) por teclado
clave = int(input('Ingrese la clave: '))
minutos = int(input('Ingrese el numero de minutos: '))

"""
Con un bucle while se creara un menu y segun la clave se evalua el costo
"""
while clave == 12:
    costo = minutos*2
    break
while clave == 15:
    costo = minutos*2.2
    break
while clave == 18:
    costo = minutos*4.5
    break
while clave == 19:
    costo = minutos*3.5
    break
while clave == 23:
    costo = minutos*6
    break
while clave == 15:
    costo = minutos*6
    break
while clave == 29:
    costo = minutos*5
    break

# Se da formato al mensaje por pantalla con fstring
print(f"Costo total de la llamada {costo:,.0f}")