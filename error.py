class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        elif self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje}: {self.dimension} excede el máximo de {self.maximo}"
        elif self.dimension is not None:
            return f"{self.mensaje}: dimensión {self.dimension} no válida"
        else:
            return f"{self.mensaje}: máximo {self.maximo}"
