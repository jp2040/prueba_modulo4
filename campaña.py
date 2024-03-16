# campaña.py

from anuncio import Video, Display, Social, SubTipoInvalidoException

class Campaña:
    """
    Clase que representa una campaña publicitaria que contiene una lista de anuncios.
    """
    def __init__(self, nombre, anuncios):
        """
        Constructor de la clase Campaña.

        Parámetros:
            nombre (str): El nombre de la campaña.
            anuncios (list): Lista de diccionarios que contienen información sobre los anuncios.
        """
        self.nombre = nombre
        self._anuncios = []
        for anuncio_info in anuncios:
            tipo = anuncio_info['tipo']
            if tipo == 'Video':
                anuncio = Video(sub_tipo=anuncio_info['sub_tipo'])
            elif tipo == 'Display':
                anuncio = Display(sub_tipo=anuncio_info['sub_tipo'])
            elif tipo == 'Social':
                anuncio = Social(sub_tipo=anuncio_info['sub_tipo'])
            else:
                raise ValueError("Tipo de anuncio no válido")
            self._anuncios.append(anuncio)

    @property
    def anuncios(self):
        """
        Propiedad anuncios para obtener la lista de anuncios de la campaña.
        """
        return self._anuncios

    @property
    def nombre(self):
        """
        Propiedad nombre para obtener el nombre de la campaña.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Setter de la propiedad nombre para establecer el nombre de la campaña.

        Parámetros:
            value (str): El valor del nombre de la campaña.
        
        Raise:
            LargoExcedidoException: Si el nombre excede los 250 caracteres.
        """
        if len(value) <= 250:
            self._nombre = value
        else:
            raise LargoExcedidoException("El nombre excede los 250 caracteres.")

    def __str__(self):
        """
        Método especial para obtener una representación en cadena de la campaña.
        """
        anuncios_count = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            if isinstance(anuncio, Video):
                anuncios_count["Video"] += 1
            elif isinstance(anuncio, Display):
                anuncios_count["Display"] += 1
            elif isinstance(anuncio, Social):
                anuncios_count["Social"] += 1
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {anuncios_count['Video']} Video, {anuncios_count['Display']} Display, {anuncios_count['Social']} Social"


class LargoExcedidoException(Exception):
    """
    Excepción personalizada para cuando el largo del nombre de la campaña excede los 250 caracteres.
    """
    pass
