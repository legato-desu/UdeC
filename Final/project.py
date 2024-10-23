from matplotlib import pyplot
import math

# Función cuadrática.
def f1(x):
    return x**2
# Función lineal.
def f2(x):
    return x+3
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-5, 5)
pyplot.ylim(-5, 5)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()

"""


# Función cuadrática.
def f1(x):
        
    funcion = int(input("Ingreso: "))
# Función lineal.

# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-5, 5)
pyplot.ylim(-5, 5)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()
"""