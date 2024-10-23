import sys
from matplotlib import pyplot
import numpy as np

# Verifica cuántos argumentos se pasaron
if len(sys.argv) > 2:
    funcion1 = sys.argv[1]
    funcion2 = sys.argv[2]
else:
    funcion1 = sys.argv[1]
    funcion2 = None  # No hay segunda función

# Definir la primera función evaluando la expresión ingresada
def f1(x):
    return eval(funcion1)

# Si existe la segunda función, definirla
if funcion2:
    def f2(x):
        return eval(funcion2)

# Definir el rango de x
x = np.linspace(-10, 10, 100)

# Graficar la primera función
y1 = [f1(i) for i in x]
pyplot.plot(x, y1, label=f'f(x) = {funcion1}')

# Si hay una segunda función, graficarla
if funcion2:
    y2 = [f2(i) for i in x]
    pyplot.plot(x, y2, label=f'f(x) = {funcion2}')

# Dibujar los ejes y mostrar la gráfica
pyplot.axhline(0, color="black")  # Línea del eje x
pyplot.axvline(0, color="black")  # Línea del eje y
pyplot.legend()
pyplot.show()