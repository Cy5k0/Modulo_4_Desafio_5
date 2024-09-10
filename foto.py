from error import DimensionError


class Foto:
    """Clase que representa una fotografía con dimensiones de ancho y alto.

    Attributes:
        MAX (int): El valor máximo permitido para el ancho y alto de la fotografía.
        ancho (int): El ancho de la fotografía.
        alto (int): El alto de la fotografía.
        __ruta (str): La ruta de la imagen.
    """

    MAX = 2500

    def __init__(self, ruta: str, ancho: int, alto: int) -> None:
        """Inicializa una instancia de la clase Foto.

        Args:
            ancho (int): El ancho de la fotografía.
            alto (int): El alto de la fotografía.
            ruta (str): La ruta del archivo de imagen.

        Raises:
            DimensionError: Si el ancho o alto están fuera del rango permitido.
        """
        self.ancho = ancho
        self.alto = alto
        self._ruta = ruta

    @property
    def ruta(self):
        return self._ruta

    @ruta.setter
    def ruta(self, value):
        self._ruta = value

    @property
    def ancho(self) -> int:
        """Obtiene el ancho de la fotografía.

        Returns:
            int: El ancho de la fotografía.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """Establece el ancho de la fotografía.

        Args:
            ancho (int): El nuevo ancho de la fotografía.

        Raises:
            DimensionError: Si el nuevo ancho está fuera del rango permitido.
        """
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Ancho no válido", ancho, Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """Obtiene el alto de la fotografía.

        Returns:
            int: El alto de la fotografía.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """Establece el alto de la fotografía.

        Args:
            alto (int): El nuevo alto de la fotografía.

        Raises:
            DimensionError: Si el nuevo alto está fuera del rango permitido.
        """
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Alto no válido", alto, Foto.MAX)
        else:
            self.__alto = alto


try:
    strruta = str(input("Ingrese ruta de la imagen: "))
    int_ancho = int(input("Ingrese ancho de la imagen: "))
    int_alto = int(input("Ingrese alto de la imagen: "))
    # print(f"xxx:{strruta}")

    fotos = Foto(strruta, int_ancho, int_alto)
    print(f"alto de la foto: {fotos.alto}")
    print(f"ancho de la foto: {fotos.ancho}")
    print(f"ruta de la foto: {fotos.ruta}")

    int_ancho = int(input("Ingrese nuevo ancho de la imagen: "))
    int_alto = int(input("Ingrese nuevo alto de la imagen: "))

    fotos.ancho = int_ancho
    print(f"ancho de la foto: {fotos.ancho}")
    fotos.alto = int_alto
    print(f"alto de la foto: {fotos.alto}")

except DimensionError as e:
    print(e)
except ValueError:
    print("\nHa ocurrido un error al ingresar los valores")
except Exception as e:
    print(f"\nHa ocurrido un error inesperado: {e}")
