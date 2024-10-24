# Proyecto Integrador - Graficador de Funciones

Este proyecto es una aplicación gráfica desarrollada en Python que permite graficar funciones matemáticas. La aplicación utiliza la biblioteca `Tkinter` para crear una interfaz gráfica (GUI) desde donde se ingresan las funciones, y `Matplotlib` para graficarlas. Además, permite evaluar y graficar múltiples funciones de manera simultánea.

## Funcionalidades

- **Ingreso de Funciones**: Los usuarios pueden ingresar hasta dos funciones matemáticas en la interfaz.
- **Evaluación y Graficación**: El programa evalúa y grafica las funciones ingresadas dentro de un rango predefinido de valores para la variable `x`.
- **Manejo de errores**: Si no se ingresan funciones o si se intenta graficar una expresión inválida, se muestra un mensaje de error.
- **Salida Gráfica**: La salida gráfica incluye la representación de las funciones junto con los ejes y una cuadrícula.

## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje principal del proyecto.
- **Tkinter**: Para crear la interfaz gráfica de usuario (GUI).
- **Matplotlib**: Para la visualización y graficación de las funciones.
- **Numpy**: Para la manipulación eficiente de datos numéricos.

## Estructura del Proyecto

```bash
- ├── integrador.
- │   ├── ventana.py       # Código de la interfaz gráfica para ingresar las funciones.
- │   ├── graficas.py      # Código para graficar las funciones ingresadas.
- ├── README.md            # Descripción del proyecto.
- ├── requirements.txt     # Lista de dependencias necesarias.
```
## Cómo Ejecutar el Proyecto

### Requisitos previos

1. Asegúrate de tener instalado Python 3.x en tu sistema.
2. Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
## Ejecución
1. Abre una terminal en el directorio raíz del proyecto.
2. Ejecuta el archivo ventana.py para iniciar la interfaz gráfica:
   ```bash
   python integrador/ventana.py
3. Ingresa una o dos funciones matemáticas en los cuadros de texto y presiona el botón "GRAFICAR".
4. La gráfica se generará y se mostrará en una nueva ventana.

## Ejemplos de Uso
### Entrada
- Supongamos que ingresas las siguientes funciones en la interfaz gráfica:
- - sin(x)
- - x^2
### Salida
- La aplicación generará un gráfico con ambas funciones, mostrando la sinusoide de sin(x) y la parábola de x^2 dentro del rango de x de -10 a 10.

## Capturas de Pantalla
Aquí puedes incluir imágenes de la interfaz gráfica y del gráfico generado para que los usuarios vean cómo luce la aplicación en ejecución.

```markdown
![Ventana Inicial (Sin Datos)](Capturas/Ventana%20inicial%20(vacia).png)
![Ventana Error](Capturas/Ventana%20error.png)
![Ventana Inicial (Con Datos)](Capturas/Ventana%20inicial%20(con%20datos).png)
![Ventana de Graficos](Capturas/Ventana%20de%20graficos.png)

![Ventana error](C:\Users\Phantom\Documents\Developer\Python\UdeC\Integrador\Capturas de Pantalla)
```
## Problemas Conocidos
- **Errores de sintaxis:** Si ingresas una función con un formato incorrecto, el programa no podrá graficarla.
- **Rango de gráficos:** Actualmente, las gráficas están limitadas a un rango de -10 a 10 tanto para x como para y. En futuras versiones se podría hacer ajustable.

## Contribuciones
Si deseas contribuir al proyecto, siéntete libre de hacer un fork y abrir un pull request. También puedes abrir un issue si encuentras algún bug o tienes sugerencias de mejoras.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
