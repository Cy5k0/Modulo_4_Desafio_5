class DimensionError(Exception):
    """Excepción personalizada para errores de dimensión en una fotografía.

    Esta excepción se lanza cuando las dimensiones (ancho o alto) de una fotografía
    no son válidas, es decir, están fuera del rango permitido.

    Attributes:
        mensaje (str): El mensaje de error.
        dimension (int, optional): La dimensión que causó el error (puede ser ancho o alto).
        maximo (int, optional): El valor máximo permitido para la dimensión.
    """

    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        """Inicializa una instancia de DimensionError.

        Args:
            mensaje (str): El mensaje de error.
            dimension (int, optional): La dimensión que causó el error (puede ser ancho o alto).
            maximo (int, optional): El valor máximo permitido para la dimensión.
        """
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        """Devuelve una representación en cadena del error.

        Returns:
            str: El mensaje de error detallado.
        """
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        elif self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje}: {self.dimension} excede el máximo de {self.maximo}"
        elif self.dimension is not None:
            return f"{self.mensaje}: dimensión {self.dimension} no válida"
        else:
            return f"{self.mensaje}: máximo {self.maximo}"
