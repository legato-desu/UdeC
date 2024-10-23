import sys
from matplotlib import pyplot
import numpy as np

# Obtener las funciones pasadas desde ventana.py
funcion1 = sys.argv[1]
funcion2 = sys.argv[2]

# Definir la primera función evaluando la expresión ingresada
def f1(x):
    return eval(funcion1)

# Definir la segunda función evaluando la expresión ingresada
def f2(x):
    return eval(funcion2)

# Definir el rango de x
x = np.linspace(-10, 10, 100)

# Graficar ambas funciones
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]

pyplot.plot(x, y1, label=f'f(x) = {funcion1}')
pyplot.plot(x, y2, label=f'f(x) = {funcion2}')
pyplot.axhline(0, color="black")  # Línea del eje x
pyplot.axvline(0, color="black")  # Línea del eje y
pyplot.legend()
pyplot.show()





"""
window = tkinter.Tk()
    
window.title("Funciones A & D")
window.geometry("280x100")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


# Función cuadrática.
def f1(funcion_1_entry):    
    return funcion_1_entry

def grafi(event):
    
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


def exit(event):
    window.quit()


funcion_1_label = ttk.Label(window, text="1° Funcion:")
funcion_1_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

funcion_1_entry = ttk.Entry(window)
funcion_1_entry.grid(column=1, row=0, sticky=tkinter.E, padx=20, pady=5)

funcion_2_label = ttk.Label(window, text="2° Funcion:")
funcion_2_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)


funcion_2_entry = ttk.Entry(window)
funcion_2_entry.grid(column=1, row=1, sticky=tkinter.E, padx=20, pady=5)

boton_grafica = ttk.Button(window, text="GRAFICAR")
boton_grafica.grid(column=1, row=3, sticky=tkinter.E, padx=20, pady=5)
boton_grafica.bind("<Button-1>",grafi)

boton_salida = ttk.Button(window, text="SALIR")
boton_salida.grid(column=0, row=3, sticky=tkinter.E, padx=20, pady=5)
boton_salida.bind("<Button-1>",exit)
boton_salida.quit()


window.mainloop()"""