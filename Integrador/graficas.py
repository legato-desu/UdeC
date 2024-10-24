import sys
import matplotlib.pyplot as plt
import numpy as np
import math

# Obtener las funciones ingresadas como argumentos desde ventana.py
funciones = sys.argv[1:]  # Toma los argumentos pasados al script, que son las funciones ingresadas

# Rango de valores de x
x = np.linspace(-10, 10, 400)  # Crea un arreglo de 400 valores entre -10 y 10

# Crear la figura para las gráficas
plt.figure()  # Inicia una nueva figura de gráfico

# Función para evaluar las expresiones ingresadas
def evaluar_funcion(funcion, x):
    # Reemplazar potencias y funciones matemáticas conocidas por su versión en Python
    funcion = funcion.replace("^", "**")  # Cambia el símbolo de potencia de '^' a '**'
    funcion = funcion.replace("sin", "math.sin")  # Asocia la función trigonométrica seno
    funcion = funcion.replace("cos", "math.cos")  # Asocia la función trigonométrica coseno
    funcion = funcion.replace("tan", "math.tan")  # Asocia la función trigonométrica tangente
    funcion = funcion.replace("exp", "math.exp")  # Asocia la función exponencial
    funcion = funcion.replace("log", "math.log")  # Asocia la función logaritmo

    # Evaluar la función en el contexto de las funciones matemáticas (math y np)
    return [eval(funcion, {"x": xi, "math": math, "np": np}) for xi in x]  # Evalúa la función para cada valor de x

# Graficar cada función ingresada
for funcion in funciones:
    try:
        y = evaluar_funcion(funcion, x)  # Calcula los valores de y para la función actual
        plt.plot(x, y, label=f"y = {funcion}")  # Grafica la función y agrega una etiqueta
    except Exception as e:
        print(f"Error al graficar {funcion}: {e}")  # Si ocurre un error, lo imprime

# Añadir etiquetas y líneas del eje
plt.axhline(0, color="black",linewidth=1)  # Línea horizontal en y=0 (eje x)
plt.axvline(0, color="black",linewidth=1)  # Línea vertical en x=0 (eje y)
plt.xlim(-10, 10)  # Limita los valores del eje x de -10 a 10
plt.ylim(-10, 10)  # Limita los valores del eje y de -10 a 10
plt.legend()  # Muestra la leyenda para identificar las funciones graficadas
plt.title("Funcion Graficada")  # Título del gráfico
plt.grid(True)  # Activa la cuadrícula en el gráfico

# Guardar la gráfica como imagen y mostrarla
plt.savefig("output.png")  # Guarda la imagen del gráfico en un archivo "output.png"
plt.show()  # Muestra el gráfico en pantalla