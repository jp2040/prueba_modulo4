# anuncio.py
from abc import ABC, abstractmethod

class Anuncio:
    """
    Clase abstracta que representa un anuncio genérico.
    """
    SUB_TIPOS = ()  # Se define en las subclases específicas

    def __init__(self, alto=1, ancho=1, sub_tipo=None):
        """
        Constructor de la clase Anuncio.

        Parámetros:
            alto (int): La altura del anuncio.
            ancho (int): El ancho del anuncio.
            sub_tipo (str): El subtipo del anuncio.
        """
        self._alto = alto if alto > 0 else 1
        self._ancho = ancho if ancho > 0 else 1
        self.sub_tipo = sub_tipo

    @property
    def alto(self):
        """
        Propiedad alto para obtener la altura del anuncio.
        """
        return self._alto

    @alto.setter
    def alto(self, value):
        """
        Setter de la propiedad alto para establecer la altura del anuncio.

        Parámetros:
            value (int): El valor de la altura del anuncio.
        """
        self._alto = value if value > 0 else 1

    @property
    def ancho(self):
        """
        Propiedad ancho para obtener el ancho del anuncio.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        """
        Setter de la propiedad ancho para establecer el ancho del anuncio.

        Parámetros:
            value (int): El valor del ancho del anuncio.
        """
        self._ancho = value if value > 0 else 1

    @property
    def sub_tipo(self):
        """
        Propiedad sub_tipo para obtener el subtipo del anuncio.
        """
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        """
        Setter de la propiedad sub_tipo para establecer el subtipo del anuncio.

        Parámetros:
            value (str): El valor del subtipo del anuncio.
        
        Raise:
            SubTipoInvalidoException: Si el subtipo no es válido para el tipo de anuncio.
        """
        if value is None or value in self.SUB_TIPOS:
            self._sub_tipo = value
        else:
            raise SubTipoInvalidoException("Subtipo inválido para este tipo de anuncio.")

    @staticmethod
    def mostrar_formatos():
        """
        Método estático para mostrar los formatos de anuncios disponibles.
        """
        print("FORMATO:")
        print("==========")
        for subtipo in Anuncio.SUB_TIPOS:
            print("-", subtipo)


class Video(Anuncio):
    """
    Clase que representa un anuncio de video.
    """
    SUB_TIPOS = ("Subtipo 1", "Subtipo 2")

    def __init__(self, duracion=5, sub_tipo=None):
        """
        Constructor de la clase Video.

        Parámetros:
            duracion (int): La duración del video.
            sub_tipo (str): El subtipo del video.
        """
        super().__init__(alto=1, ancho=1, sub_tipo=sub_tipo)
        self.duracion = duracion

    @property
    def duracion(self):
        """
        Propiedad duracion para obtener la duración del video.
        """
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        """
        Setter de la propiedad duracion para establecer la duración del video.

        Parámetros:
            value (int): El valor de la duración del video.
        """
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        """
        Método para comprimir el anuncio de video.
        """
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el anuncio de video.
        """
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """
    Clase que representa un anuncio de display.
    """
    SUB_TIPOS = ("Subtipo 1", "Subtipo 2")

    def comprimir_anuncio(self):
        """
        Método para comprimir el anuncio de display.
        """
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el anuncio de display.
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    """
    Clase que representa un anuncio en redes sociales.
    """
    SUB_TIPOS = ("Subtipo 1", "Subtipo 2")

    def comprimir_anuncio(self):
        """
        Método para comprimir el anuncio en redes sociales.
        """
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Método para redimensionar el anuncio en redes sociales.
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")


class SubTipoInvalidoException(Exception):
    """
    Excepción personalizada para subtipo inválido.
    """
    pass
