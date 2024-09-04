class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
