# Calcula la poblacion estudiantil
"""
Una Universidad tiene actualmente 10000 estudiantes, se espera 
tener un crecimiento anual del 5%. Elaborar un algoritmo que 
calcule e imprima la población estudiantil que se espera 
tener en el año 2025
"""

# Asignamos una constante con el total acutal de estudiantes
estudiantes = 10000

#El buble for tendra un rango de 2021 a 2025 (4)
for i in range (2021,2025,1):
    
    """
    En cada ciclo la variable tendra un aumento multiplicando una variable 
    por otra es decir x *= 2 es equivalente a decir x = x * 2 
    
    estudiantes = estudiantes * (1 + 0.05) == estudiantes *= (1 + 0.05)
    """
    estudiantes *= (1 + 0.05)

# Con fstring se pondra puntos centena y se eliminaran los decimales 
print(f"Para 2025 se espera tener {estudiantes:,.0f} estudiantes")