from error import DimensionError


class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Ancho no válido", ancho, Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Alto no válido", alto, Foto.MAX)
        self.__alto = alto


try:
    fotos = Foto(0, 2000, "c:\\mis fotos\\xxx.jpg")
except DimensionError as e:
    print(e)


# ruta=input("Ingrese ruta de la imagen: ")
# ancho=int(input("Ingrese ancho de la imagen: "))
# alto=(input("Ingrese alto de la imagen: "))
# fotos = Foto(alto, ancho, ruta)
# ancho=int(input("Ingrese nuevo ancho de la imagen: "))
# alto=(input("Ingrese nuevo alto de la imagen: "))
# fotos.alto=alto
# fotos.ancho=ancho
