# Desafio - Manejo de Excepciones

Este proyecto es parte de un desafío de programación orientado al manejo de excepciones en Python. Se trata de una aplicación de galería de fotos que controla la modificación de las dimensiones (ancho y alto) de las fotos, asegurando que no se excedan los límites permitidos. Para esto, se utiliza una excepción personalizada llamada `DimensionError`.

## Descripción del Proyecto

El objetivo principal de este proyecto es implementar controles para que las dimensiones de las fotos (ancho y alto) no puedan ser modificadas a valores fuera del rango permitido. Para ello, se desarrolló una clase `Foto` que incluye validaciones en sus métodos setter para garantizar que los valores sean correctos. Si un valor es inválido, se lanza una excepción personalizada `DimensionError`.

### Requerimientos

1. **Excepción Personalizada:**
   - Crear una clase `DimensionError` en un archivo `error.py`, derivada de `Exception`.
   - Sobrescribir el constructor para que reciba los parámetros `mensaje`, `dimension`, y `maximo`.
   - Sobrecargar el método `__str__` para proporcionar mensajes de error detallados según los parámetros proporcionados.

2. **Clase `Foto`:**
   - Modificar los métodos setter de `ancho` y `alto` en la clase `Foto` para que lancen una excepción `DimensionError` si los valores proporcionados están fuera del rango permitido.

## Archivos Principales

### `foto.py`

Este archivo contiene la implementación de la clase `Foto`, que representa una fotografía con ancho, alto y ruta de archivo. La clase incluye validaciones en los métodos setter de `ancho` y `alto` para asegurar que los valores sean válidos.

- **Clase `Foto`:** Representa una fotografía.
  - **Atributos:**
    - `MAX` (int): Valor máximo permitido para el ancho y alto.
    - `__ancho` (int): Ancho de la fotografía.
    - `__alto` (int): Alto de la fotografía.
    - `ruta` (str): Ruta del archivo de imagen.
  - **Métodos:**
    - `ancho`: Getter y setter para el ancho de la fotografía.
    - `alto`: Getter y setter para el alto de la fotografía.

### `error.py`

Este archivo contiene la definición de la excepción personalizada `DimensionError`.

- **Clase `DimensionError`:** Excepción personalizada para manejar errores de dimensión.
  - **Atributos:**
    - `mensaje` (str): Mensaje de error.
    - `dimension` (int, opcional): Dimensión que causó el error.
    - `maximo` (int, opcional): Valor máximo permitido para la dimensión.
  - **Métodos:**
    - `__str__`: Devuelve una representación en cadena del error.

## Ejemplo de Uso

El siguiente código muestra cómo se utiliza la clase `Foto` y cómo se maneja la excepción `DimensionError`:

```python
try:
    ruta = input("Ingrese ruta de la imagen: ")
    int_ancho = int(input("Ingrese ancho de la imagen: "))
    int_alto = int(input("Ingrese alto de la imagen: "))
    fotos = Foto(int_ancho, int_alto, ruta)
    print(fotos.alto)
    print(fotos.ancho)
    int_ancho = int(input("Ingrese nuevo ancho de la imagen: "))
    int_alto = int(input("Ingrese nuevo alto de la imagen: "))

    fotos.ancho = int_ancho
    print(fotos.ancho)
    fotos.alto = int_alto
    print(fotos.alto)
except DimensionError as e:
    print(e)
except ValueError:
    print("Ha ocurrido un error al ingresar los valores")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
```



------------------------------------------

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

***Windows***

`python foto.py`

***Linux & iOS***

`python3 foto.py`

------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
