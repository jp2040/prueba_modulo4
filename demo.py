# demo.py
from anuncio import Video
from campaña import Campaña, LargoExcedidoException
from error import SubTipoInvalidoException, LargoExcedidoException

try:
    # Crear una instancia de Campaña
    anuncios_info = [
        {'tipo': 'Video', 'sub_tipo': 'Subtipo 1'},
        {'tipo': 'Display', 'sub_tipo': 'Subtipo 2'}
    ]
    campana = Campaña("Campaña de prueba", anuncios_info)

    # Modificar nombre y sub_tipo
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campana.nombre = nuevo_nombre

    nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo del anuncio de Video: ")
    for anuncio in campana.anuncios:
        if isinstance(anuncio, Video):
            anuncio.sub_tipo = nuevo_sub_tipo

except (SubTipoInvalidoException, LargoExcedidoException) as e:
    # Manejo de excepciones: escribir el error en un archivo de registro
    with open("error.log", "a") as f:
        f.write(str(e) + "\n")
