import sys
from matplotlib import pyplot
import numpy as np

# Obtener la función pasada desde el archivo ventana.py
funcion_usuario = sys.argv[1]

# Definir la función evaluando la expresión ingresada
def f(x):
    return eval(funcion_usuario)

# Definir el rango de x
x = np.linspace(-10, 15, 100)

# Graficar la función del usuario
pyplot.plot(x, [f(i) for i in x], label=f'f(x) = {funcion_usuario}')
pyplot.axhline(0, color="black")  # Línea del eje x
pyplot.axvline(0, color="black")  # Línea del eje y
pyplot.xlim(-5, 5)  # Límites del eje x
pyplot.ylim(-5, 5)  # Límites del eje y
pyplot.legend()  # Mostrar leyenda con la función
pyplot.show()
