import tkinter as tk
from tkinter import ttk
import subprocess

# Crear la ventana principal
window = tk.Tk()
window.title("Projecto Integrador")
window.geometry("320x180")
window.configure(bg='lightgray')

# Configuración de columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Instrucción para potencias
instruccion_texto = tk.Label(window, text="\tNota: para potencias x^2 = x**2", 
                            background='lightgray', font=("Arial", 8), fg="black", anchor="w")
instruccion_texto.grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

# Etiqueta de función 1
funcion1_texto = ttk.Label(window, text="Funcion 1:", background='lightgray', font=("Arial", 10, "bold"))
funcion1_texto.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada 1
funcion1_entrada = ttk.Entry(window, font=("Arial", 10))
funcion1_entrada.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Etiqueta de función 2
funcion2_texto = ttk.Label(window, text="Funcion 2:", background='lightgray', font=("Arial", 10, "bold"))
funcion2_texto.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada 2
funcion2_entrada = ttk.Entry(window, font=("Arial", 10))
funcion2_entrada.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Función para graficar
def graficar():
    funcion1 = funcion1_entrada.get()  # Obtener la primera función ingresada
    funcion2 = funcion2_entrada.get()  # Obtener la segunda función ingresada
    
    # Si ambas están vacías, no hacer nada
    if not funcion1 and not funcion2:
        print("Debe ingresar al menos una función.")
        return

    # Si solo se ingresa la primera función
    if funcion1 and not funcion2:
        subprocess.run(["py", "integrador/graficas.py", funcion1])
    # Si solo se ingresa la segunda función
    elif not funcion1 and funcion2:
        subprocess.run(["py", "integrador/graficas.py", funcion2])
    # Si ambas funciones están llenas
    else:
        subprocess.run(["py", "integrador/graficas.py", funcion1, funcion2])

# Botón de graficar
boton_grafica = ttk.Button(window, text="GRAFICAR", width=10, command=graficar)
boton_grafica.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

# Botón de salida
boton_salir = ttk.Button(window, text="SALIR", width=10, command=window.quit)
boton_salir.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

window.mainloop()