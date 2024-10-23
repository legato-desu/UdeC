import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
window = tk.Tk()
window.title("Projecto Ingetrador")
window.geometry("320x150")
window.configure(bg='lightgray')  # Color de fondo similar al de la imagen

# Configuración de columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Cuadro de texto explicativo
instruction_label = tk.Label(window, text="\tNota: para potencias x^2 = x**2", 
                            background='lightgray', font=("Arial", 8), fg="black", anchor="w")
instruction_label.grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

# Etiqueta de función 1
function_label = ttk.Label(window, text="FUNCION 1:", background='lightgray', font=("Arial", 10, "bold"))
function_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada 1
function_entry = ttk.Entry(window, font=("Arial", 10))
function_entry.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Etiqueta de función 2
function_label = ttk.Label(window, text="FUNCION 2:", background='lightgray', font=("Arial", 10, "bold"))
function_label.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

# Cuadro de entrada 2
function_entry = ttk.Entry(window, font=("Arial", 10))
function_entry.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10, ipadx=30)

# Botón de graficar
graph_button = ttk.Button(window, text="GRAFICAR", width=10)
graph_button.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

# Botón de salida
exit_button = ttk.Button(window, text="EXIT", width=10, command=window.quit)
exit_button.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

window.mainloop()