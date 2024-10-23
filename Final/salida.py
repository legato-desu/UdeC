# Entrada

import tkinter
from tkinter import ttk

window = tkinter.Tk()
    
window.title("Funciones A & D")
window.geometry("280x100")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = ttk.Label(window, text="1° Funcion:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=20, pady=5)

"""password_label = ttk.Label(window, text="2° Funcion:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window)
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=20, pady=5)"""

login_button = ttk.Button(window, text="GRAFICAR")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=20, pady=5)

botonexit = ttk.Button(window, text="EXIT")
botonexit.grid(column=0, row=3, sticky=tkinter.E, padx=20, pady=5)
botonexit.bind("<Button-1>",exit)
botonexit.quit()


window.mainloop()