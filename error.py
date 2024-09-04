class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje}: {self.dimension} (máximo permitido: {self.maximo})"
        return self.mensaje
