# Promedio salarial
"""
Si una persona recibe por un salario por trabajar 30 dias y 8 horas
dias determine el salario si:
1. Si el salario es 1.800.000 y trabaja 15 mas 6 horas cual es el salario
2. Si el salario es 1.500.000 y trabaja 80 horas con recargo del 25% y 40 horas 
    de recargo del 35% cual es el salario
3. si el salario es 1.600.000 y trabaja 2 semanas mas 3 dias + 7 horas 
    con un descuento de 10% por cada hora trabajada cual es el salario
"""
# Se pide al usuario que ingrese por teclado el salario a calcular
salario = int(input('Ingrese el salario: '))

# Segun el salario ingresado se hara su respectivo calculo 
if salario == 1800000:
    dia = salario / 30 # Promedio por dias
    hora = dia / 8 # Promedio por horas
    total_1 = (dia * 15 + hora * 6) + salario
    total_2 = (dia * 15 + hora * 6)
    print(f"El salario: ${salario:,.0f} tendra un monto de: ${total_2:,.0f}")
    print(f"Por 15 dias y 6 horas para un total de: ${total_1:,.0f}")

elif salario == 1500000:
    dia = salario / 30
    hora = dia / 8
    recargo_1 = ((hora*80)*0.25)+hora*80
    recargo_2 = ((hora*40)*0.35)+hora*40
    total_1 = salario + recargo_1 + recargo_2
    total_2 = recargo_1 + recargo_2 
    print(f"El salario: ${salario:,.0f} tendra un monto de: ${total_2:,.0f}")
    print(f"Por un recargo de 80hrs (25%) y 40hrs (35%) es de: ${total_1:,.0f}")

elif salario == 1600000:
    dia = (salario / 30)
    hora = dia / 8
    recargo = (hora * 7)
    descuento = (salario + ((dia * 17) + recargo))
    total_2 = ((dia * 17) + recargo)
    total_1 = descuento - (descuento*0.10)
    print(f"El salario: ${salario:,.0f} tendra un monto de: ${total_2:,.0f}")
    print(f"Mas 14 dias y 7 hrs con 10% de descuento: ${total_1:,.0f}")

else:
    print('Salario no registrado')