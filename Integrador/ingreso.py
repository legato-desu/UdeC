import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import messagebox  # Importar el módulo para mostrar alertas emergentes

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title("Projecto Integrador")  # Título de la ventana
window.geometry("320x180")  # Tamaño de la ventana
window.configure(bg='lightgray')  # Color de fondo de la ventana

# Configuración de columnas para la disposición de widgets
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

<<<<<<< HEAD
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
=======
# Etiqueta para la primera función
funcion1_texto = ttk.Label(window, text="Funcion 1:", background='lightgray', font=("Arial", 10, "bold"))
funcion1_texto.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada para la primera función
funcion1_entrada = ttk.Entry(window, font=("Arial", 10))  # Corregido: asignado a una nueva variable
funcion1_entrada.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Etiqueta para la segunda función
funcion2_texto = ttk.Label(window, text="Funcion 2:", background='lightgray', font=("Arial", 10, "bold"))
funcion2_texto.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada para la segunda función
funcion2_entrada = ttk.Entry(window, font=("Arial", 10))
funcion2_entrada.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Información en la parte inferior de la ventana
informacion_texto = tk.Label(window, text="Andres Granja\t\t\tDavid Miranda", 
                            background='lightgray', font=("Arial", 8), fg="black", anchor="w")
informacion_texto.grid(column=0, row=4, columnspan=2, sticky=tk.W, padx=10, pady=5)

# Función que se ejecuta al presionar el botón "GRAFICAR"
def graficar():
    funcion1 = funcion1_entrada.get()  # Corregido: obtener la primera función desde el cuadro correcto    funcion2 = funcion2_entrada.get()  # Obtener la segunda función ingresada
    
    # Si ambas entradas están vacías, se muestra una alerta
    if not funcion1 and not funcion2:
        messagebox.showwarning("ERROR", "Debe ingresar al menos una función.")  # Alerta de error
        return

    # Ejecutar el archivo `graficas.py` con los argumentos dependiendo de las funciones ingresadas
    if funcion1 and not funcion2:
        subprocess.run(["py", "integrador/graficas.py", funcion1])  # Ejecutar con la primera función
    elif not funcion1 and funcion2:
        subprocess.run(["py", "integrador/graficas.py", funcion2])  # Ejecutar con la segunda función
    else:
        subprocess.run(["py", "integrador/graficas.py", funcion1, funcion2])  # Ejecutar con ambas funciones

<<<<<<< HEAD
# Botón de graficar
boton_grafica = ttk.Button(window, text="GRAFICAR", width=10, command=graficar)
boton_grafica.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

# Botón de salida
=======
# Botón para graficar las funciones ingresadas
boton_graficar = ttk.Button(window, text="GRAFICAR", width=10, command=graficar)
boton_graficar.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

# Botón de salida para cerrar la aplicación
>>>>>>> 8e4be5f288e0dc9ae54ae2fd9c7e18bd577e3fcc
boton_salir = ttk.Button(window, text="SALIR", width=10, command=window.quit)
boton_salir.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

# Iniciar el loop principal de la ventana
window.mainloop()