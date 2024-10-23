import tkinter as tk
from tkinter import ttk
import subprocess

# Crear la ventana principal
window = tk.Tk()
window.title("Funciones A & D")
window.geometry("320x180")
window.configure(bg='lightgray')

# Configuración de columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Etiqueta de función
function_label = ttk.Label(window, text="FUNCION:", background='lightgray', font=("Arial", 10, "bold"))
function_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada
function_entry = ttk.Entry(window, font=("Arial", 10))
function_entry.grid(column=1, row=0, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Cuadro de texto explicativo
instruction_label = tk.Label(window, text="Nota: Use ^= para potencias (Ej: x^2 = x**2)", 
                            background='lightgray', font=("Arial", 8), fg="black", anchor="w")
instruction_label.grid(column=0, row=1, columnspan=2, sticky=tk.W, padx=10, pady=5)

# Función para graficar
def graficar():
    funcion = function_entry.get()  # Obtener la función ingresada
    # Llama a graficas.py y pasa la función como argumento
    subprocess.run(["py", "ome\graficas.py", funcion])

# Botón de graficar
graph_button = ttk.Button(window, text="GRAFICAR", width=10, command=graficar)
graph_button.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

# Botón de salida
exit_button = ttk.Button(window, text="EXIT", width=10, command=window.quit)
exit_button.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

window.mainloop()