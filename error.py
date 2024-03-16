# error.py

class SubTipoInvalidoException(Exception):
    """
    Excepción que se levanta cuando se proporciona un subtipo inválido.
    """
    pass

class LargoExcedidoException(Exception):
    """
    Excepción que se levanta cuando el largo de una cadena excede un límite específico.
    """
    pass
